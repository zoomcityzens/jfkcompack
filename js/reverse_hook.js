$(function () {
  let debug = false;
  let baseUrl = debug
    ? "http://localhost:8000/api/v1/"
    : "https://jfkcompack.pythonanywhere.com/api/v1/";
  let carList = document.querySelector("#carList");
  let carForm = $("#carForm");

  // *getting adnd submiiting form
  $(carForm).on("submit", (e) => {
    e.preventDefault();
    let formData = {};
    $(carForm)
      .serializeArray()
      .forEach(({ name, value }) => (formData[name] = value));

    let url = `${baseUrl}cars_request/`;
    fetch(url, {
      method: 'POST',
      body: JSON.stringify(formData),
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data)
        alert('Form Submitted successfully')
      })
      .catch( err => console.error('A problem occurred while submitting form', err))
  });

  // Display all cars
  if (carList) {
    displayAllCars()
      .then((data) => {
        if (data.length > 0){
          data.forEach((car) => {
            carList.innerHTML += `
          <div class="col-sm-12 col-md-3">
                <div class="team-member card p-4 m-4">
                  <div class="thumb-post">
                    <img src="${car.image}" alt="" loading="lazy" />
                    <span class="member-role">Brand New</span>
                  </div>
                  <div class="member-content">
                    <h5><a href="">${car.title}</a></h5>
                    <p><small>Duis vitae consequat neque. Nulla pharetra eleifend nulla. </small></p> 
                  </div>
                  <div class="action-section">
                    <!-- Button trigger modal -->
                    <button
                      type="button"
                      class="action-btn text-center dynamicCardBtn"
                      data-toggle="modal"
                      data-target="#staticBackdrop"
                      data-type="cardBtn"
                      onclick="document.getElementById('hiddenCarId').setAttribute('value', '${car.id}')"
                    >
                      Select
                    </button>
                  </div>
                </div>
                <!-- /.team-member -->
              </div>
          `;
          });
        }
        else{
          console.log('Yello');
          carList.innerHTML = `
            <div class="col-12">
                <h3 class="text-center text-muted"> We are so sorry there are no cars for sale yet <h3>
            </div>
          `;
        }
      })
      .catch((err) => console.log(err));
  }

  // -----------------------------------------------------------------
  // --------------------- Functions ---------------------------------
  // -----------------------------------------------------------------

  async function getCars(id) {
    let url = `${baseUrl}/get/car/${id}/`;
    let car = (await fetch(url)).json();
    return car;
  }

  async function displayAllCars() {
    let url = `${baseUrl}cars/`;
    let cars = (await fetch(url)).json();
    return cars;
  }
});
