import { Nav, NavLink, NavMenu } from "./NavbarElements";

const Navbar = () => {
    return (


        <Nav>
            <NavMenu>
                /* Navigation links - Home (defaault), and image Upload page */
                <NavLink to="/">Home</NavLink>
                <NavLink to="/image_upload">Image Upload</NavLink>
            </NavMenu>
        </Nav>
    );
};

export default Navbar;

