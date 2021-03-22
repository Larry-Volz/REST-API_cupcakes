$(document).ready(()=>{

    getCupcakes();


    let  new_cc={};

    //Get data from form -> on(submit), prevent default
    $("#cupcake-form").on("submit", (evt)=>{
        evt.preventDefault();
        
         new_cc.flavor=$('#flavor').val()
         new_cc.size=$('#size').val()
         new_cc.rating=$('#rating').val()
         new_cc.image=$('#image').val()


        
        //Modify structure of new_cc, JSONify + send to route to JSONify & add a cupcake
        let data = add_cupcake(new_cc);
            console.log(data);
            
        });
    
});

// *************************************** FUNCTION DEFINITIONS *************************************************
    
async function getCupcakes() {
    /** GET ALL CUPCAKES LIST FROM API/UPDATE DOM */
    let res = await axios.get('/api/cupcakes');

    let arrayOfCupcakes = res.data.cupcakes;

    // ***REMEMBER use for OF not for IN!!! ***
    let txt=""
    for (cupcake of arrayOfCupcakes) {
        txt+= build_cc_4_dom(cupcake);
    }
    
    $('.cupcake-display').append(txt);
    
}
async function add_cupcake(new_cc) {

    // ********** THIS LINE IS CRITICAL TO MAKE SURE JSON FORMAT WORKS!!! ***********************
    cc_for_api = {"cupcake": new_cc}
    console.log("cc_for_api STRUCTURE = ", cc_for_api);

    // stringified_cc = JSON.stringify(cc_for_api);
    // console.log("STRINGIFIED=", stringified_cc)

    let res = await axios.post(`/api/cupcakes`, cc_for_api).then(function(){

        //append cupcake data to the DOM
        txt = build_cc_4_dom(new_cc);
        $('.cupcake-display').append(txt);
        
        document.getElementById("cupcake-form").reset();
    });
    
}

function build_cc_4_dom(cupcake){
    /**  BUILD HTML FOR DOM UPDATE OF EACH CUPCAKE */
    let txt="";
            txt +=`<div class="card m-2" style="width: 14rem; display: inline-block;">`
            txt += `<img class="card-img-top"  alt="card image cap" src="${cupcake.image}">`;
            txt += `<div class="card-body"><h2>${cupcake.flavor}</h2>`;
            txt += `<ul><li>Rating: ${cupcake.rating}</li>`;
            txt += `<li>Size: ${cupcake.size}</li><ul></div></div>`;
        return txt;
        }
