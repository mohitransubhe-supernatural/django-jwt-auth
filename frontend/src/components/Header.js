import React, {useContext} from "react";
import {Link} from "react-router-dom";
import AuthContext from "../context/AuthContext";

const Header = () => {
    let {user, logoutUser} = useContext(AuthContext)
    return (
        <div>
            <Link to="/">Home</Link>
            <span> | </span>
            {
                user ? (
                    <p onClick={logoutUser} style={{'cursor': 'pointer'}}>Logout</p>
                ) : (
                    <React.Fragment>
                        <Link to="/login">Login</Link>
                        <span> | </span>
                        <Link to="/register">Register</Link>
                    </React.Fragment>
                )
            }

            {user && <p>Hello {user.username}</p>}
        </div>
    )
}

export default Header