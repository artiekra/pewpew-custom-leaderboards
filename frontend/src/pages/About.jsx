import './About.css'

const About = () => {
    return(
        <div className="about">
            <h2>Welcome to PewPew Live&apos;s custom leaderboard!</h2>
            <br />
            <div className="block1">
                <h3>What have we done?</h3>
                <br />
                <p>This project started as a way to improve the gameplay for PewPew Live players (and we were also bored). 
                    Here you can find UP-TO-DATE information about your points, compare your skills with other players, and view graphs! (Wow)</p>
            </div>
            <div className="block2">
                <h3>Open source</h3>
                <br />
                <p>Our leaderboard is an open source project developed with passion and dedication (sometimes). So you can look at the source code <a href="https://github.com/artiekra/pewpew-custom-leaderboards" target='_blank' rel="noopener noreferrer">here</a></p>
            </div>
            <div className="block3">
                <h3>Our team</h3>
                <br />
                <p>We&apos;re, just a couple of gamers and developers who like PewPew Live. Well, besides, this site looks good for the new game update!</p>
            </div>
            <div className="block4">
                <h3>Connect with us</h3>
                <br />
                <p>If you have any questions, suggestions or just want to say hello, please contact us:</p>
                <br />
                <br />
                <p>Artemii Kravchuk: <a href="https://t.me/Ch4l0v4k" target="_blank" rel="noopener noreferrer">Telegram</a></p>
                <br />
                <p>Chelovek_01: <a href="https://t.me/artiekra" target="_blank" rel="noopener noreferrer">Telegram</a></p>
            </div>
            <br />
            <br />
            <p className='thank'>Thank you for visiting and we hope you enjoy the leaderboard!</p>
        </div>
    );
};

export default About