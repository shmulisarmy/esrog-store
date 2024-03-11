function Esrog({id, size, clarity, odor_strength, texture_smoothness, ripeness_score, image_url}){
    return(
        <div class="esrog">
            <img onClick={() => window.open(image_url)} src={image_url} alt="could not load"/>
            <div className="text">
                <p>Esrog: {id}</p>
                <p>Size: {size}</p>
                <p>Clarity: {clarity}</p>
                <p>Odor: {odor_strength}</p>
                <p>Texture: {texture_smoothness}</p>
                <p>Ripeness: {ripeness_score}</p>
            </div>
        </div>
    )
}


function App({esrog_data}){
    return(
        <main>
            {esrog_data.map(esrog_json => <Esrog {...esrog_json}/>)}    
        </main>
    )
}

async function load_data(){
    const response = await fetch('all_esrog_data');
    const esrog_data = await response.json();
    console.log(esrog_data);
    ReactDOM.render(<App {...{esrog_data}}/>, document.getElementById('root'));
}

load_data();