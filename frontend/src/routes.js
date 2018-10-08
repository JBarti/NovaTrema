import React from 'react';
import { BrowserRouter } from 'react-router-dom'
import { Route, Switch } from 'react-router'
import App from './App.jsx'
import Naslovnica from './pages/naslovnica/Naslovnica.jsx'
import Novosti from './pages/novosti/Novosti.jsx'

export default (
    <BrowserRouter>
        <Switch>
            <Route exact path='/naslovnica' component={Naslovnica} />
            <Route exact path='/novosti' component={Novosti} />
            <Route exact path='/test' component={App} />
        </Switch>
    </BrowserRouter>
)