// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider } from "firebase/auth";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyDe1xwESCHcIsHW2RD4RGeqBMjVF9FH1ww",
  authDomain: "whatsapp-clone-d7143.firebaseapp.com",
  projectId: "whatsapp-clone-d7143",
  storageBucket: "whatsapp-clone-d7143.appspot.com",
  messagingSenderId: "892036761559",
  appId: "1:892036761559:web:551ed146347f04fd31ad92",
  measurementId: "G-46RDH5SLVK"
};

// Initialize Firebase
const firebaseApp = initializeApp(firebaseConfig);
const auth = getAuth(firebaseApp);
const goggleAuthProvider = new GoogleAuthProvider();

// Initialize Cloud Firestore and get a reference to the service
const db = getFirestore(firebaseApp);

export { auth, goggleAuthProvider, db };
