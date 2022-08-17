import React, { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'

import "./styles.css"

export default function WatchView()
{
  const [items, fetchVideo] = useState([])
  const params = useParams()

  const getData = () => {
    fetch('http://127.0.0.1:8000/rest/watch/'+params.id)
      .then(res => res.json())
      .then(res => {
        fetchVideo(res)
        console.log(res)
      });
  }

  useEffect(() => { getData() }, [])


  return (
    <>
    {
      items.map(item => (
        <video width="1080" height="720" className="video-fluid" autoPlay controls>
        <source src={'http://localhost:8000' + item.video} type="video/mp4" />
        </video>
      ))
    }
    </>
  );
}
