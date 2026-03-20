// ============================================================
// SERVICE WORKER — Predictive Health Risk PWA v2
// Caches all pages so the app works 100% offline after first visit
// ============================================================

const CACHE_NAME = 'health-risk-v2';
const OFFLINE_URL = '/offline';

// Files to cache immediately when app is first installed
const PRECACHE_URLS = [
  '/',
  '/login',
  '/register',
  '/calculators',
  '/assess',
  '/dashboard',
  '/offline',
  '/nearby',
  '/about',
  '/static/manifest.json',
  '/static/css/style.css',
  // Bootstrap 5 CDN
  'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css',
  'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js',
  // Font Awesome icons
  'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css',
  // Chart.js
  'https://cdn.jsdelivr.net/npm/chart.js',
  // Google Fonts
  'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap',
];

// ── INSTALL: Cache all essential files ──────────────────────
self.addEventListener('install', event => {
  console.log('[SW] Installing Health Risk PWA v2...');
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      console.log('[SW] Pre-caching app shell');
      return Promise.allSettled(
        PRECACHE_URLS.map(url =>
          cache.add(url).catch(err => console.warn('[SW] Failed to cache:', url, err))
        )
      );
    }).then(() => self.skipWaiting())
  );
});

// ── ACTIVATE: Clean old caches ──────────────────────────────
self.addEventListener('activate', event => {
  console.log('[SW] Activating v2...');
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames
          .filter(name => name !== CACHE_NAME)
          .map(name => {
            console.log('[SW] Deleting old cache:', name);
            return caches.delete(name);
          })
      );
    }).then(() => self.clients.claim())
  );
});

// ── FETCH: Serve from cache, fall back to network ───────────
self.addEventListener('fetch', event => {
  const { request } = event;
  const url = new URL(request.url);

  // Skip non-GET and browser extension requests
  if (request.method !== 'GET') return;
  if (url.protocol === 'chrome-extension:') return;
  // Skip Google Maps API calls (must be live)
  if (url.hostname.includes('maps.googleapis.com') || url.hostname.includes('maps.google.com')) return;

  // Strategy: Cache-first for static assets
  if (
    url.pathname.startsWith('/static/') ||
    url.hostname.includes('cdn.jsdelivr.net') ||
    url.hostname.includes('cdnjs.cloudflare.com') ||
    url.hostname.includes('unpkg.com') ||
    url.hostname.includes('fonts.googleapis.com') ||
    url.hostname.includes('fonts.gstatic.com')
  ) {
    event.respondWith(
      caches.match(request).then(cached => {
        if (cached) return cached;
        return fetch(request).then(response => {
          if (response && response.status === 200) {
            const clone = response.clone();
            caches.open(CACHE_NAME).then(cache => cache.put(request, clone));
          }
          return response;
        }).catch(() => new Response('', { status: 503 }));
      })
    );
    return;
  }

  // Strategy: Network-first for HTML pages (so data is always fresh)
  if (request.headers.get('accept') && request.headers.get('accept').includes('text/html')) {
    event.respondWith(
      fetch(request)
        .then(response => {
          if (response && response.status === 200) {
            const clone = response.clone();
            caches.open(CACHE_NAME).then(cache => cache.put(request, clone));
          }
          return response;
        })
        .catch(() => {
          return caches.match(request).then(cached => {
            if (cached) return cached;
            return caches.match(OFFLINE_URL);
          });
        })
    );
    return;
  }

  // Strategy: Network-first for API calls
  if (url.pathname.startsWith('/api/')) {
    event.respondWith(
      fetch(request)
        .then(response => response)
        .catch(() => {
          return new Response(
            JSON.stringify({
              error: 'offline',
              message: 'You are offline. Please reconnect to submit data.'
            }),
            { status: 503, headers: { 'Content-Type': 'application/json' } }
          );
        })
    );
    return;
  }

  // Default: Network with cache fallback
  event.respondWith(
    fetch(request)
      .then(response => {
        if (response && response.status === 200) {
          const clone = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(request, clone));
        }
        return response;
      })
      .catch(() => caches.match(request).then(cached => cached || caches.match(OFFLINE_URL)))
  );
});

// ── SYNC: Background sync when internet returns ─────────────
self.addEventListener('sync', event => {
  if (event.tag === 'sync-health-data') {
    console.log('[SW] Background sync triggered');
    event.waitUntil(syncPendingData());
  }
});

async function syncPendingData() {
  console.log('[SW] Syncing pending health data to server...');
}

// ── PUSH: Notifications for daily health reminders ──────────
self.addEventListener('push', event => {
  const data = event.data ? event.data.json() : {};
  const title = data.title || 'Health Reminder 💊';
  const options = {
    body: data.body || 'Time to log your daily health metrics!',
    icon: '/static/icons/icon-192.png',
    badge: '/static/icons/icon-192.png',
    vibrate: [200, 100, 200],
    data: { url: data.url || '/tracker' },
    actions: [
      { action: 'open', title: 'Log Now' },
      { action: 'dismiss', title: 'Later' }
    ]
  };
  event.waitUntil(self.registration.showNotification(title, options));
});

self.addEventListener('notificationclick', event => {
  event.notification.close();
  if (event.action !== 'dismiss') {
    event.waitUntil(clients.openWindow(event.notification.data.url || '/'));
  }
});