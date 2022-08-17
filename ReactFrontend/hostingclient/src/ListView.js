import React from 'react'

import "./styles.css"

export default function ListView(props)
{
  return (
    <ul>
    {
      props.items.map(item => (
        <li key={item.pk}>
            <a align="center" className="nav-link" href={'/watch/'+ item.pk}>
               <video width="320" height="240" className="video-fluid">
                <source src={'http://localhost:8000' + item.video} type="video/mp4" />
              </video>
              <br />
              <p className="text-center mt-2 mb-2">{ item.name }</p>
            </a>
          <hr />
        </li>
      ))
    }
    </ul>
  );
}
