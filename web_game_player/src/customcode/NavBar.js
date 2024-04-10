export default function Navbar() {
    return ( 
    <nav className="nav">
        <a href="/" className="site-title">
            GAME REALM
        </a>
            <ul>
                <CustomLink href="/Games">Games</CustomLink>
                <CustomLink href="/Account">Login/Sign Up</CustomLink>
            </ul>
    </nav>
    )
}

function CustomLink({href, children, ...props}) {
    const path = window.location.pathname
    
    return (
        <li className={path === href ? "active" : ""}>
            <a href={href} {...props}>{children}</a>
        </li>
    )
}