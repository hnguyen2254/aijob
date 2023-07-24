// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyC64b_3k2aWRmta_GOa6DSEnjuTRoIUZhw",
  authDomain: "ai-job-board.firebaseapp.com",
  projectId: "ai-job-board",
  storageBucket: "ai-job-board.appspot.com",
  messagingSenderId: "160391549467",
  appId: "1:160391549467:web:95c5a2b30de21f86991ebe",
  measurementId: "G-1474YV6T13"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);