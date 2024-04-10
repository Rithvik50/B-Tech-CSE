import Navbar from "./customcode/NavBar";
import Games from "./customcode/Games";
import Home from "./customcode/Home";

function App() {
  let component
  switch (window.location.pathname) {
    case "/":
      component = <Home />
      break
    case "/Games":
      component = <Games />
      break
  }
  return (
    <>
    <Navbar />
    <div className="Container">{component}</div>
    </>
  )

}

export default App;