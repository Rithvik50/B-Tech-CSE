import React, { Component } from 'react';
import './App.css';

class App extends Component {
  constructor() {
    super();
    this.state = {
      orderItems: [
        {
          id: 1,
          name: 'MAC book',
          description: 'Apple MGN63HNA\nMacBook Air (Apple MI\nChip/8GB/256GB SSD/macOS Big\nSur/Retina) INR',
          price: 90000,
          quantity: 0,
        },
        {
          id: 2,
          name: 'Dell core i7',
          description: '11th  Generation Intel Core i7-11390H\n Processor Windows 11 Home INR',
          price: 80000,
          quantity: 0,
        },
        {
          id: 3,
          name: 'HP',
          description: '11th generation INR',
          price: 65000,
          quantity: 0,
        },
      ],
    };
  }

  handleQuantityChange = (id, increment) => {
    const updatedOrderItems = this.state.orderItems.map((item) => {
      if (item.id === id) {
        item.quantity += increment;
      }
      return item;
    });

    this.setState({
      orderItems: updatedOrderItems,
    });
  };

  calculateTotalCost = () => {
    let total = 0;
    this.state.orderItems.forEach((item) => {
      total += item.price * item.quantity;
    });

    return total;
  };

  render() {
    const styles = {
      item: {
        border: '1px solid #ccc',
        padding: '10px',
        margin: '10px',
      },
    };

    return (
      <div id="order-summary" style={styles}>
        <h1>Order Summary</h1>
        <div className="order-items">
          {this.state.orderItems.map((item) => (
            <div key={item.id} style={styles.item} className="order-item">
              <div>
                <strong>{item.name}</strong>
              </div>
              <div>
                Description: <br />
                <div className="description">{item.description}</div>
              </div>
              <div>Price: {item.price} INR</div>
              <div>
                Quantity: {item.quantity}<br/>
                <button
                  className="increment-button"
                  onClick={() => this.handleQuantityChange(item.id, 1)}
                >
                  +
                </button>
              </div>
            </div>
          ))}
        </div>
        <div className="total-cost">
          <strong>Total: {this.calculateTotalCost()} INR</strong>
        </div>
      </div>
    );
  }
}

export default App;