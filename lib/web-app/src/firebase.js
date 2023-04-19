import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "XXXXXXXXXXXXXXXXXXXXX",
  authDomain: "XXXXXXXXXXXXXXXX",
  projectId: "XXXXXXXXXXXXXXXXXXXX",
  storageBucket: "XXXXXXXXXXXXX",
  messagingSenderId: "XXXXXXXXXXXXXXXXXXX",
  appId: "1:XXXXXXXXXXXXXXXX:web:XXXXXXXXXXXXXXXXXXX",
  measurementId: "G-XXXXXXXXXXX"
};

const app = initializeApp(firebaseConfig);

const db = getFirestore(app);
const auth = getAuth(app);

export { db, auth};