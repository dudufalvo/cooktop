import { BrowserRouter, Route, Routes } from "react-router-dom";
import React from 'react'
import { AuthContext } from "./components/AuthContext";
import LoginPage from "./pages/LoginPage/LoginPage"
import HomePage from "./pages/HomePage/HomePage"

function App() {
  const useAuth = React.useContext(AuthContext);
  const userToken = useAuth.state.userToken;
  
  return (
    <BrowserRouter>
      <Routes>
      {!userToken ? (
            <Route index element={<LoginPage />} />
        ) : (
          <>
            <Route path="/home/" element={<HomePage />} />
          </>
        )}
      </Routes>
    </BrowserRouter>
  );
}

export default App;