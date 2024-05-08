import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [restaurants, setRestaurants] = useState([]);
  const [newRestaurant, setNewRestaurant] = useState({
    rest_name: '',
    rest_id: '',
    rest_addr: '',
    rest_reviews: 0,
    food_menu: [],
  });
  const [updateGrade, setUpdateGrade] = useState({
    rest_id: '',
    rest_reviews: 0,
  });
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:3000/restaurants')
      .then(response => setRestaurants(response.data))
      .catch(error => console.error('Error fetching restaurants:', error));
  }, []);

  const handleAddRestaurant = () => {
    axios.post('http://localhost:3000/restaurants', newRestaurant)
      .then(response => {
        setRestaurants([...restaurants, response.data]);
        setNewRestaurant({
          rest_name: '',
          rest_id: '',
          rest_addr: '',
          rest_reviews: 0,
          food_menu: [],
        });
      })
      .catch(error => {
        console.error('Error adding restaurant:', error);
        if (error.response) {
          console.error('Server responded with status:', error.response.status);
          console.error('Response data:', error.response.data);
          setError(`Server responded with status ${error.response.status}. Please check the server logs.`);
        } else if (error.request) {
          console.error('No response received from the server.');
          setError('No response received from the server. Please check the server logs.');
        } else {
          console.error('Error setting up the request:', error.message);
          setError('Error setting up the request. Please check the server logs.');
        }
      });
  };

  const handleUpdateGrade = () => {
    axios.put(`http://localhost:3000/restaurants/${updateGrade.rest_id}`, { rest_reviews: updateGrade.rest_reviews })
      .then(response => {
        setRestaurants(restaurants.map(restaurant => (restaurant.rest_id === updateGrade.rest_id ? response.data : restaurant)));
        setUpdateGrade({
          rest_id: '',
          rest_reviews: 0,
        });
      })
      .catch(error => {
        console.error('Error updating grade:', error);
        if (error.response) {
          console.error('Server responded with status:', error.response.status);
          console.error('Response data:', error.response.data);
          setError(`Server responded with status ${error.response.status}. Please check the server logs.`);
        } else if (error.request) {
          console.error('No response received from the server.');
          setError('No response received from the server. Please check the server logs.');
        } else {
          console.error('Error setting up the request:', error.message);
          setError('Error setting up the request. Please check the server logs.');
        }
      });
  };

  return (
    <div>
      <h1>Restaurant App</h1>
      <h2>Restaurants</h2>
      <ul>
        {restaurants.map(restaurant => (
          <li key={restaurant.rest_id}>
            {restaurant.rest_name} - Grade: {restaurant.rest_reviews}
          </li>
        ))}
      </ul>
      <h2>Add New Restaurant</h2>
      <div>
        <label>Name:</label>
        <input type="text" value={newRestaurant.rest_name} onChange={e => setNewRestaurant({ ...newRestaurant, rest_name: e.target.value })} />
      </div>
      <div>
        <label>ID:</label>
        <input type="text" value={newRestaurant.rest_id} onChange={e => setNewRestaurant({ ...newRestaurant, rest_id: e.target.value })} />
      </div>
      <div>
        <label>Address:</label>
        <input type="text" value={newRestaurant.rest_addr} onChange={e => setNewRestaurant({ ...newRestaurant, rest_addr: e.target.value })} />
      </div>
      <div>
        <label>Grade:</label>
        <input type="number" value={newRestaurant.rest_reviews} onChange={e => setNewRestaurant({ ...newRestaurant, rest_reviews: e.target.value })} />
      </div>
      <div>
        <label>Food Menu:</label>
        <input type="text" value={newRestaurant.food_menu} onChange={e => setNewRestaurant({ ...newRestaurant, food_menu: e.target.value.split(',') })} />
      </div>
      <button onClick={handleAddRestaurant}>Add Restaurant</button>

      <h2>Update Restaurant Grade</h2>
      <div>
        <label>ID:</label>
        <input type="text" value={updateGrade.rest_id} onChange={e => setUpdateGrade({ ...updateGrade, rest_id: e.target.value })} />
      </div>
      <div>
        <label>New Grade:</label>
        <input type="number" value={updateGrade.rest_reviews} onChange={e => setUpdateGrade({ ...updateGrade, rest_reviews: e.target.value })} />
      </div>
      <button onClick={handleUpdateGrade}>Update Grade</button>

      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
}

export default App;
