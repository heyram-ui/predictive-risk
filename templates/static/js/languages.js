// languages.js — Multi-language support
const LANGUAGES = {
    en: {
        dashboard:    "Dashboard",
        nearby:       "Nearby Hospitals",
        assess:       "Health Check",
        profile:      "Profile",
        logout:       "Logout",
        search:       "Search",
        hospitals:    "Hospitals",
        pharmacies:   "Pharmacies",
        loading:      "Loading...",
        error:        "Something went wrong.",
        noResults:    "No results found.",
        openNow:      "Open Now",
        closed:       "Closed",
        rating:       "Rating",
        distance:     "Distance",
        getDirections:"Get Directions",
        callNow:      "Call Now"
    },
    ta: {
        dashboard:    "டாஷ்போர்டு",
        nearby:       "அருகில் உள்ள மருத்துவமனைகள்",
        assess:       "உடல்நல பரிசோதனை",
        profile:      "சுயவிவரம்",
        logout:       "வெளியேறு",
        search:       "தேடு",
        hospitals:    "மருத்துவமனைகள்",
        pharmacies:   "மருந்தகங்கள்",
        loading:      "ஏற்றுகிறது...",
        error:        "ஏதோ தவறு நடந்தது.",
        noResults:    "முடிவுகள் இல்லை.",
        openNow:      "இப்போது திறந்திருக்கிறது",
        closed:       "மூடப்பட்டது",
        rating:       "மதிப்பீடு",
        distance:     "தூரம்",
        getDirections:"வழிகாட்டுதல் பெறு",
        callNow:      "இப்போது அழைக்கவும்"
    },
    hi: {
        dashboard:    "डैशबोर्ड",
        nearby:       "नज़दीकी अस्पताल",
        assess:       "स्वास्थ्य जाँच",
        profile:      "प्रोफ़ाइल",
        logout:       "लॉगआउट",
        search:       "खोजें",
        hospitals:    "अस्पताल",
        pharmacies:   "फार्मेसी",
        loading:      "लोड हो रहा है...",
        error:        "कुछ गलत हुआ।",
        noResults:    "कोई परिणाम नहीं मिला।",
        openNow:      "अभी खुला है",
        closed:       "बंद है",
        rating:       "रेटिंग",
        distance:     "दूरी",
        getDirections:"दिशा-निर्देश पाएं",
        callNow:      "अभी कॉल करें"
    }
};

// Apply language to page
function applyLanguage(lang) {
    const t = LANGUAGES[lang] || LANGUAGES['en'];
    document.querySelectorAll('[data-lang]').forEach(function(el) {
        var key = el.getAttribute('data-lang');
        if (t[key]) el.textContent = t[key];
    });
    localStorage.setItem('phr_language', lang);
}

// Load saved language on page load
document.addEventListener('DOMContentLoaded', function () {
    var saved = localStorage.getItem('phr_language') || 'en';
    var selector = document.getElementById('languageSelector');
    if (selector) selector.value = saved;
    applyLanguage(saved);
});