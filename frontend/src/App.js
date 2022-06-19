import{BrowserRouter as Router,Routes,Route} from 'react-router-dom'
import {About} from './components/About'
import { User } from './components/User';
import {Navbar} from './components/Navbar'

function App() {
  return (
  <Router>
    <Navbar></Navbar>
    <div className='container p-4'>
      <Routes>
        <Route path='/About' element={<About/>}></Route>
        <Route path='/' element={<User/>}></Route>
      </Routes>

    </div>
  </Router>

   
  );
}

export default App;
