import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { getAuth, createUserWithEmailAndPassword } from 'firebase/auth';
import { getFirestore, doc, setDoc } from 'firebase/firestore';
import { Link } from 'react-router-dom';

import SignIn from './SignIn';
import './SignIn.css';

const citiesDict = {
  'Tirana': 'TIA',
 'Graz': 'GRZ',
 'Innsbruck': 'INN',
 'Brussels': 'CRL',
 'Paphos': 'PFO',
 'Tallinn': 'TLL',
 'Helsinki': 'HEL',
 'Turku': 'TKU',
 'Lille': 'LIL',
 'Lyon': 'LYS',
 'Paris': 'ORY',
 'Kutaisi': 'KUT',
 'Dresden': 'DRS',
 'Leipzig': 'LEJ',
 'Munich': 'MUC',
 'Athens': 'ATH',
 'Chania': 'CHQ',
 'Santorini': 'JTR',
 'Thessaloniki': 'SKG',
 'Knock, County Mayo': 'NOC',
 'County Kerry': 'KIR',
 'Cagliari': 'CAG',
 'Catania': 'CTA',
 'Naples': 'NAP',
 'Olbia': 'OLB',
 'Trapani': 'TPS',
 'Venice': 'TSF',
 'Kaunas': 'KUN',
 'Vilnius': 'VNO',
 'Oslo': 'TRF',
 'Stavanger': 'SVG',
 'Warsaw': 'WMI',
 'Timișoara': 'TSR',
 'Niš': 'INI',
 'Málaga': 'AGP',
 'Alicante': 'ALC',
 'Almería': 'LEI',
 'Asturias': 'OVD',
 'Bilbao': 'BIO',
 'Barcelona': 'BCN',
 'Badajoz': 'BJZ',
 'Béziers': 'BZR',
 'Brindisi': 'BDS',
 'Donostia / San Sebastián': 'EAS',
 'Fuerteventura': 'FUE',
 'Girona': 'GRO',
 'Granada': 'GRX',
 'Ibiza': 'IBZ',
 'Jerez de la Frontera': 'XRY',
 'A Coruña': 'LCG',
 'Lanzarote': 'ACE',
 'Madrid': 'MAD',
 'Agadir': 'AGA',
 'Menorca': 'MAH',
 'Melilla': 'MLN',
 'Palma, Majorca': 'PMI',
 'Pamplona': 'PNA',
 'Santander': 'SDR',
 'Seville': 'SVQ',
 'Tenerife': 'TFS',
 'Valencia': 'VLC',
 'Valladolid': 'VLL',
 'Vigo': 'VGO',
 'Vitoria-Gasteiz': 'VIT',
 'Valverde': 'VDE',
 'Zaragoza': 'ZAZ',
 'Santiago de Compostela': 'SCQ'
};

const SignUp = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [location, setLocation] = useState('');
  const [error, setError] = useState(null); // add state variable
  const navigate = useNavigate();

  const handleSignUp = async (e) => {
    e.preventDefault();
    const auth = getAuth();
    try {
      const userCredential = await createUserWithEmailAndPassword(auth, email, password);
      const userId = userCredential.user.uid;
      const db = getFirestore();
      await setDoc(doc(db, 'users', userId), {
        email,
        location,
        userId,
        password
      });
      navigate('/');
    } catch (error) {
      setError(error.message);

    }
  };

  return (
    <div className="form-container">
      <h1>Sign Up</h1>
      {error && <div className="error">{error}</div>} {/* render error message if error state is not null */}
      <form onSubmit={handleSignUp}>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <select value={location} onChange={(e) => setLocation(e.target.value)} required>
          <option value="">Select your location</option>
          {Object.entries(citiesDict).map(([city, code]) => (
            <option key={code} value={code}>
              {city}
            </option>
          ))}
        </select>
        <button type="submit">Sign Up</button>
      </form>
      <Link className="back-button" to="/">Back to Sign In</Link>
    </div>
  );
};


export default SignUp;
