import React from 'react';
import {IconContext} from 'react-icons';
import {FaLinkedin, FaAngellist, FaGithub} from 'react-icons/fa';
import { MdWeb } from "react-icons/md";
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
                    {/* Austin */}
                    <div className="footer-col-row1">
                        <img className="footer-profilePic" src="/Austin.jpg"/>
                        <h3>Austin Keumper</h3>
                        <div className="footer-row-row2">
                        <a href="https://github.com/AKuemper" target="_blank"><FaGithub/></a>
                        <a href="https://angel.co/u/austin-kuemper" target="_blank"><FaAngellist/></a>
                        <a href="https://github.com/AKuemper" target="_blank"><MdWeb/></a>
                        <a href="https://www.linkedin.com/in/austin-kuemper-0b471b84/" target="_blank"><FaLinkedin/></a>
                    </div>
                    </div>
                    {/* Jubin */}
                    <div className="footer-col-row1">
                        <img className="footer-profilePic" src="/Jubin.png"/>
                        <h3>Jubin Taghdir</h3>
                        <div className="footer-row-row2">
                        <a href="https://github.com/Jubintgh" target="_blank"><FaGithub/></a>
                        <a href="https://angel.co/u/jubin-taghdir" target="_blank"><FaAngellist/></a>
                        <a href="https://github.com/Jubintghr" target="_blank"><MdWeb/></a>
                        <a href="https://www.linkedin.com/in/jubintaghdir/" target="_blank"><FaLinkedin/></a>
                    </div>
                    </div>
                    {/* Matt */}
                    <div className="footer-col-row1">
                        <img className="footer-profilePic" src="/Matt.jpg"/>
                        <h3>Matthew Melendez</h3>
                        <div className="footer-row-row2">
                        <a href="https://github.com/melendezmatt" target="_blank"><FaGithub/></a>
                        <a href="https://angel.co/u/matthew-melendez-1" target="_blank"><FaAngellist/></a>
                        <a href="https://github.com/melendezmatt" target="_blank"><MdWeb/></a>
                        <a href="https://www.linkedin.com/in/matthew-melendez/" target="_blank"><FaLinkedin/></a>
                    </div>
                    </div>
                    {/* Tony */}
                    <div className="footer-col-row1">
                        <img className="footer-profilePic" src="/Tony.jpg"/>
                        <h3>Tony Costanza</h3>
                        <div className="footer-row-row2">
                        <a href="https://github.com/AnthonyCost" target="_blank"><FaGithub/></a>
                        <a href="https://angel.co/u/anthony-costanza-1" target="_blank"><FaAngellist/></a>
                        <a href="https://anthonycost.github.io/portfolio/" target="_blank"><MdWeb/></a>
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
