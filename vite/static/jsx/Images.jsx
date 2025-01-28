export default Carosel;
 
 function Carosel(path, alt, caption)
{
    return  (
        <>
            <Image
                source ={path}
                alt = {alt}
                caption ={caption}
            />
                
            <div id="img-btn" className="btn-container">
                <button id ="prev-btn" className="img-btn" >
                    <i className="bi bi-arrow-left-square-fill"></i>
                </button>
                <button id ="next-btn" className="img-btn" >
                    <i className="bi bi-arrow-right-square-fill"></i>
                </button>
            </div>
        </>);
}

function Image({source, alt, caption})
{
    console.log(alt);
    let test = source;
    return (
        <>
            <img 
                id="car-img"
                alt={alt}
                src={test}
                
            />
            <div className="caption">
                <p>{caption}</p>
            </div>
        </>
    );
}

