import React, { useState, useEffect } from 'react'

import ListView from './ListView'

export default function SubscriptionView()
{
  const [items, fetchVideo] = useState([])

  const getData = () => {
    fetch('http://127.0.0.1:8000/rest/subscriptions')
      .then(res => res.json())
      .then(res => {
        fetchVideo(res)
      });
  }

  useEffect(() => { getData() }, [])
  
  return (
    <>
    <h3 align="center">Подписки</h3>
    <ListView items={items}/>
    </>
  );
}
