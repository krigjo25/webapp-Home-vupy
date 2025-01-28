export default Carosel;
 
 function Carosel(path, alt, caption)
{
    console.log(arg);
    return  (
        <>
            <Image
                
                source ={path}
                alt = {alt}
                caption ={caption}
            />
                
            <div id="img-btn" class="btn-container">
                <button id ="prev-btn" class="img-btn" onClick="prev()">
                    <i className="bi bi-arrow-left-square-fill"></i>
                </button>
                <button id ="next-btn" className="img-btn"onClick="next()">
                    <i className="bi bi-arrow-right-square-fill"></i>
                </button>
            </div>
        </>);
}

function Image({source, alt, caption})
{
    return (
        <>
            <img 
                id="car-img" 
                src={source} 
                alt={alt} 
            />
            <div class="caption">
                <p>${caption}</p>
            </div>
        </>
    );
}

