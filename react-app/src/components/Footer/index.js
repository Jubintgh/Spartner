import React from 'react';
import {IconContext} from 'react-icons';
import {FaLinkedin, FaGithub} from 'react-icons/fa';
import "./Footer.css";

const Footer = () => {
    return (
        <div className="main-footer">
<IconContext.Provider value={{ className: 'react-icons'}}>
            <div className="footer-container">
                <div className="footer-title-container">
                <img src="https://user-images.githubusercontent.com/35717793/126367109-4954f04b-0cb7-4ca9-a25a-d18e6b7cb74a.png" className="spartnerFooterLogo"/>
                <h3 className="footer-title"> was a collaboration by:</h3>
                </div>
                <div className="footer-content-row-1">
                    {/* column1 */}
                    <div className="footer-col-row1">
                        <img className="footer-profilePic" src="/images/Austin.jpg"/>
                        <h3>Austin Keumper</h3>
                        <div className="footer-row-row2">
                        <a href="https://github.com/AKuemper" target="_blank"><FaGithub/></a>
                        <a href="https://www.linkedin.com/in/austin-kuemper-0b471b84/" target="_blank"><FaLinkedin/></a>
                        </div>
                    </div>
                    {/* column2 */}
                    <div className="footer-col-row1">
                        <img className="footer-profilePic" src="/images/PlaceholderProfile.png"/>
                        <h3>Jubin Taghdir</h3>
                        <div className="footer-row-row2">
                        <a href="https://github.com/Jubintgh" target="_blank"><FaGithub/></a>
                        <a href="https://www.linkedin.com/in/jubintaghdir/" target="_blank"><FaLinkedin/></a>
                    </div>
                    </div>
                    {/* column3 */}
                    <div className="footer-col-row1">
                        <img className="footer-profilePic" src="/images/PlaceholderProfile.png"/>
                        <h3>Matthew Melendez</h3>
                        <div className="footer-row-row2">
                        <a href="https://github.com/melendezmatt" target="_blank"><FaGithub/></a>
                        <a href="https://www.linkedin.com/in/matthew-melendez/" target="_blank"><FaLinkedin/></a>
                    </div>
                    </div>
                    {/* column4 */}
                    <div className="footer-col-row1">
                        <img className="footer-profilePic" src="/images/Tony.jpg"/>
                        <h3>Tony Costanza</h3>
                        <div className="footer-row-row2">
                        <a href="https://github.com/AnthonyCost" target="_blank"><FaGithub/></a>
                        <a href="https://www.linkedin.com/in/anthony-costanza-64952820a/" target="_blank"><FaLinkedin/></a>
                    </div>
                    </div>
                </div>
                </div>
                    </IconContext.Provider>
        </div>
        )
}

export default Footer;