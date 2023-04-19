import React, { useState, useEffect } from 'react';
import './HomePage.css';
import TinderCard from 'react-tinder-card';

const dummyData = [
  {
    id: 1,
    title: 'Example Title 1',
    description: 'Example Description 1',
    imageUrl: 'https://via.placeholder.com/300x200',
  },
];

const HomePage = () => {
  const [showModal, setShowModal] = useState(false);
  const [selectedFlight, setSelectedFlight] = useState(null);
  const [showTutorial, setShowTutorial] = useState(true);

  useEffect(() => {
    setTimeout(() => {
      setShowTutorial(false);
    }, 5000);
  }, []);

  const swiped = (direction, id) => {
    console.log('You swiped:', direction, id);
  };

  const outOfFrame = (id) => {
    console.log('You swiped all cards:', id);
  };

  const showFlightDetails = (flight) => {
    setSelectedFlight(flight);
    setShowModal(true);
  };

  const closeModal = () => {
    setShowModal(false);
  };

  const hideTutorial = () => {
    setShowTutorial(false);
  };

  return (
    <div className="home-page">
      <div className="recommendation-cards-container">
        {dummyData.map((data) => (
          <TinderCard
            key={data.id}
            className="swipe"
            onSwipe={(dir) => swiped(dir, data.id)}
            onCardLeftScreen={() => outOfFrame(data.id)}
            onClick={() => showFlightDetails(data)}
          >
            <div
              style={{ backgroundImage: `url(${data.imageUrl})` }}
              className="card"
            >
              <h3>{data.title}</h3>
              <p>{data.description}</p>
              <button
                className="show-details-button"
                onClick={(e) => {
                  e.stopPropagation();
                  showFlightDetails(data);
                }}
              >
                Show Details
              </button>
            </div>
          </TinderCard>
        ))}
      </div>

      {showModal && (
        <div className="flight-details-modal" onClick={closeModal}>
          <div className="flight-details-container">
            <h3>{selectedFlight.title}</h3>
            <p>{selectedFlight.description}</p>
          </div>
        </div>
      )}

      {showTutorial && (
        <div className="swipe-tutorial" onClick={hideTutorial}>
          <div>
            <p className="swipe-tutorial-text">
              Swipe right for like, left for dislike
            </p>
            <div className="arrow-container">
              <div className="arrow arrow-left"></div>
              <div className="arrow arrow-right"></div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default HomePage;
