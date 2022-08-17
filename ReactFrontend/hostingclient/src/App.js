import React from 'react'

import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';

import './styles.css';

import BaseView from './BaseView';
import SubscriptionView from './SubscriptionView';
import RecommendationView from './RecommendationView';
import MyVideoView from './MyVideoView';
import WatchView from './WatchView';

export default function App()
{  
  return (
      <div className="App">
      <BrowserRouter>
              <nav className="navbar navbar-expand-lg navbar-dark bg-dark static-top">
           <div className="container">
               <Link className="nav-link" to="/">MyTube</Link>
               <button className="navbar-toggler" type="button" data-toggle="collapse"
                       data-target="#navbarResponsive"
                       aria-controls="navbarResponsive" aria-expanded="false"
                       aria-label="Toggle navigation">
                   <span className="navbar-toggler-icon"></span>
               </button>
               <div className="collapse navbar-collapse" id="navbarResponsive">
                   <ul className="navbar-nav ml-auto">
                     <li className="nav-item active">
                       <Link className="nav-link" to="/subscriptions">Мои подписки</Link>
                     </li>
                     <li className="nav-item active">
                         <Link className="nav-link" to="/recommendations">Рекомендации</Link>
                     </li>
                     <li className="nav-item active">
                         <Link className="nav-link" to="/myvideos">Мои видео</Link>
                     </li>
                   </ul>
               </div>
           </div>
        </nav>
        <Routes>
          <Route exact path="/" element={<BaseView/>} />
          <Route path="/subscriptions" element={<SubscriptionView />} />
          <Route path="/recommendations" element={<RecommendationView />} />
          <Route path="/myvideos" element={<MyVideoView />} />
          <Route path="/watch/:id" element={<WatchView />} />
        </Routes>
        </BrowserRouter>
      </div>
  );
}
