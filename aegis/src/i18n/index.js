import i18n from "i18next";
import LangueageDetector from "i18next-browser-languagedetector";
import { initReactI18next } from "react-i18next";
import en from "./en.json";
import tr from "./tr.json";

i18n.use(LangueageDetector)
    .use(initReactI18next)
    .init({
        lng: localStorage.getItem("i18nextLng") || "en",
        resources: {
            en: { translation: en },
            tr: { translation: tr },
        },
        debug: true,
        fallbackLng: "en",
        interpolation: {
            escapeValue: false,
        },
    });

export default i18n;
