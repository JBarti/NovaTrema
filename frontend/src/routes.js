import React from 'react';
import { BrowserRouter } from 'react-router-dom'
import { Route, Switch } from 'react-router'
import App from './App.jsx'
import Naslovnica from './pages/naslovnica/Naslovnica.jsx'

export default (
    <BrowserRouter>
        <Switch>
            <Route path='/naslovnica' component={Naslovnica} />
            <Route path='/test' component={App} />
        </Switch>
    </BrowserRouter>
)