function Esrog({ id, estimated_price, image_url, video_url, reserved }) {
  return (
    <div class="esrog">
      <img
        onClick={() => {
          play_video(video_url);
        }}
        src={image_url}
        alt="could not load"
      />
      <div className="text">
        <h1>Esrog #{id}</h1>
        <h1>estimated price: {`$${estimated_price}`}</h1>
        {reserved ? (
          <h1>
            this is item is reserved but may be available tomorrow if not bought
            be then
          </h1>
        ) : <button onClick={() => { reserve(id) }}>reserve</button>}
      </div>
    </div>
  );
}

function Video_component({ url }) {
  return (
    <iframe width="512" height="480" src={url} allowfullscreen></iframe>
  );
}

function Esrogim({ esrog_data }) {
  return (
    <main>
      {esrog_data.map((esrog_json) => (
        <Esrog {...esrog_json} />
      ))}
    </main>
  );
}

async function load_data() {
  min_price = document.querySelector("#min_price").value;
  max_price = document.querySelector("#max_price").value;
  texture_smoothness = document.querySelector("#texture_smoothness").value;
  size = document.querySelector("#size").value;
  ripeness_score = document.querySelector("#ripeness_score").value;
  console.log(max_price, min_price);
  if (!min_price || !max_price) {
    url = "all_esrog_data?";
  } else if (min_price > max_price) {
    alert("min price cannot be greater than max price");
    return;
  } else {
    url = `price_filter/${min_price}/${max_price}`;
  }

  added_values = false;

  if (parseInt(texture_smoothness) > 0) {
    regex()
    url = `${url}texture_smoothness=${texture_smoothness}`;
  }
  if (parseInt(size) > 0) {
    regex()
    url = `${url}size=${size}`;
  }
  if (parseInt(ripeness_score) > 0) {
    regex()
    url = `${url}ripeness_score=${ripeness_score}`;
  }

  console.log(url);
  const response = await fetch(url);
  const esrog_data = await response.json();
  console.log(esrog_data);
  ReactDOM.render(
    <Esrogim {...{ esrog_data }} />,
    document.getElementById("root")
  );
  first_fetch = false
}

function reserve(id) {
    console.log(id)
  const params = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    id: id,
  };
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  params.headers['X-CSRFToken'] = csrftoken;
  fetch('reserve', params);
}

function regex(){
    if (added_values){
        url += "&"
      } else {
        url += "?"
        added_values = true;
      }
}

function play_video(url) {
    window.scrollTo({
        top: 0,
        behavior: 'smooth' 
    });
  ReactDOM.render(
    <Video_component {...{ url }} />,
    document.querySelector("#video_player")
  );
}

let url;
let min_price;
let max_price;
let texture_smoothness;
let size;
let ripeness_score;
let added_values;
let first_fetch = true

document.querySelector("#search_form").addEventListener("keydown", (event) => {
  if (event.key == "Enter") {
    load_data();
  }
});

load_data();
