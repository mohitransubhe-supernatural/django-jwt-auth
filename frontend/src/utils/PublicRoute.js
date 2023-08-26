import {Navigate} from "react-router-dom";
import {useContext} from "react";
import AuthContext from "../context/AuthContext";

const PublicRoute = ({children, ...rest}) => {
    const user = useContext(AuthContext)
    if (user) {
        return <Navigate to="/" replace={true} />
    }
}

export default PublicRoute