import React, { Component } from 'react'

class App extends Component {
  constructor(props){
    super(props);
    this.state = {
      items: [],
      isLoaded: false,
    }
  }

  componentDidMount() {
    fetch('http://127.0.0.1:8000/rest/').then(res => res.json())
    .then(json => {
      this.setState({
          isLoaded: true,
          items: json,
      })
    });
  }
  
  render() {

    var {isLoaded, items} = this.state;

    if (!isLoaded) {
      return <div>loading...</div>;
    }


    return (
          <div className="App">
              <ul>
              {
                items.map(item => (
                  <li key={item.pk}>
                      <a href={'/watch/'+ item.pk}>
                      <video width="320" height="240">
                          <source src={'http://localhost:8000' + item.video} type="video/mp4" />
                      </video>
                      <br />
                      <p>{ item.name }</p>
                      </a>
                  </li>
                ))
              }
              </ul>
          </div>
      );
  }
}

export default App;
