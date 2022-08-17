import React, { useState, useEffect } from 'react'

import ListView from './ListView'

export default function RecommendationView()
{
  const [items, fetchVideo] = useState([])

  const getData = () => {
    fetch('http://localhost:8000/rest/recommendations')
      .then(res => res.json())
      .then(res => {
        fetchVideo(res)
      });
  }

  useEffect(() => { getData() }, [])
  
  return (
    <>
    <h3 align="center">Рекомендации</h3>
    <ListView items={items}/>
    </>
  );
}
