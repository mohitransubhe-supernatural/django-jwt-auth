import React, {useContext} from "react";
import AuthContext from "../context/AuthContext";
import { useNavigate } from 'react-router-dom';


function RegisterPage() {

  let {registerUser, authTokens} = useContext(AuthContext)

  const navigate = useNavigate()

  if (authTokens) {
      return navigate('/');
  }

  return (
    <div>
        <form onSubmit={registerUser}>
            <input type="text" name="username" placeholder="Enter Username" />
            <input type="password" name="password" placeholder="Enter Password" />
            <input type="submit" />
      </form>
    </div>
  );
}

export default RegisterPage;