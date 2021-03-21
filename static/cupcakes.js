$(document).ready(()=>{

    getCupcakes();

    
    async function getCupcakes() {
        let res = await axios.get('/api/cupcakes');

        let arrayOfCupcakes = res.data.cupcakes;
        

        // let arrayOfCupcakes = res.data.map((cc) => {
        //     // let show = tv.show;
          
        //       return  {
        //           flavor: cc.flavor,
        //           id: cc.id,
        //           image: cc.image ? show.image.medium : MISSING_IMAGE_URL,
        //           rating: cc.rating,
        //           size:cc.size
        //         };
        //     });

        // ***REMEMBER use for OF not for IN!!! ***
        let txt=""
        for (cupcake of arrayOfCupcakes) {
            // console.log(cupcake.flavor)
            txt +=`<div class="card m-2" style="width: 14rem; display: inline-block;">`
            txt += `<img class="card-img-top"  alt="card image cap" src="${cupcake.image}">`;
            txt += `<div class="card-body"><h2>${cupcake.flavor}</h2>`;
            txt += `<ul><li>Rating: ${cupcake.rating}</li>`;
            txt += `<li>Size: ${cupcake.size}</li><ul></div></div>`;
            
        }
        
        $('.cupcake-display').append(txt);
        
    }


});
    


