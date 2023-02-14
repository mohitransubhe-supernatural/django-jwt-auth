import {Navigate} from "react-router-dom";

const PrivateRoute = ({children, ...rest}) => {
    const authenticated = false
    if (authenticated) {
        return children
    }
    return (
         <Navigate to="/login" replace={true} />
    )
}

export default PrivateRoute