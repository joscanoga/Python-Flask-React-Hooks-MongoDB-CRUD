import React from "react";
import {BrowserRouter as router,Switch,Route} from "react-router-dom"
import { About } from "./components/About";
import { User } from "./components/Users";

function App() {
  return (
    <router>
      <div>
      <h1>hola mundo</h1>
        <switch>
          <Route path="/about" component={About}/>
          <Route path="/" component={User}/>
          <h1>hola mundo</h1>
        </switch>
      </div>
    </router>
  
  );
}

export default App;
