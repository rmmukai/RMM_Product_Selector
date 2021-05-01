// Add the variables in the functions. JS will look for everything from top to bottom. Alternatively you can add the the script add the bottom or after the doc is ready

function handleClickCF() {
    let cfAllProduct = document.getElementById('cf_all_product');
    let ppAllProduct = document.getElementById('pp_all_product');
    // .add adds a class to the classList
    ppAllProduct.classList.add("hide");
    // .remove removes a class from the classlist
    cfAllProduct.classList.remove("hide");

}

function handleClickPP() {
    let ppAllProduct = document.getElementById('pp_all_product');
    let cfAllProduct = document.getElementById('cf_all_product');
    cfAllProduct.classList.add("hide");
    ppAllProduct.classList.remove("hide");
}

// For reference on how to filter one option at a time

// // This will filter by the value we want. In the below case we are filtering the tensile modulus and everytime we change the drop down it does something 
// function handleTensileModulusChange(){
//     let tensile_modulus_filter = document.getElementById('tensile_modulus_filter')
//     // getElementsByClassName you are getting a list of what is in that row. 
//     let cfRows = document.getElementsByClassName('cf_row')
//     for (let row of cfRows) {
//         let data = row.getElementsByClassName('tensile-modulus')[0]
// // .innerText gets what is in between the display text. vs innerHTML which gets you whats in the HTML not just the text
//         if (data.innerText == tensile_modulus_filter.value) {
//             row.classList.remove("hide")
//         } else {
//             row.classList.add("hide")
//         }
//     } 

// }

// function handleTensileStrengthChange(){
//     let tensile_strength_filter = document.getElementById('tensile_strength_filter')
//     let cfRows = document.getElementsByClassName('cf_row')
//     for (let row of cfRows) {
//         let data = row.getElementsByClassName('tensile-strength')[0]

//         if (data.innerText == tensile_strength_filter.value) {
//             row.classList.remove("hide")
//         } else {
//             row.classList.add("hide")
//         }
//     } 

// }

// This will change when any filter is changed
function handleFilterChangeCF() {
    let tensile_modulus_filter = document.getElementById('tensile_modulus_filter')
    let tensile_strength_filter = document.getElementById('tensile_strength_filter')
    let resin_matrix_filter = document.getElementById('resin_matrix_filter')
    let carbon_fiber_processing_filter = document.getElementById('carbon_fiber_processing_filter')       
    let cfRows = document.getElementsByClassName('cf_row')

    for (let row of cfRows) {
        // These variables are retrieving the wanted data from the row specified. 
        let tensile_modulus_data = row.getElementsByClassName('tensile_modulus')[0]
        let tensile_strength_data = row.getElementsByClassName('tensile_strength')[0]
        let resin_matrix_data = row.getElementsByClassName('resin_matrix')[0]
        let carbon_fiber_processing_data = row.getElementsByClassName('carbon_fiber_processing')[0]
        let showRow = true
        
        // flipping the variable if "showRow" is false. Which means we don't want to see it. 
        // All the if statements below get ran in order, and since they aren't if/else statements they all get ran.
        // Checks to see if value is blank if it is dies not proceed to the rest of the statement. && = and, || = or
        if (tensile_modulus_filter.value && tensile_modulus_data.innerText != tensile_modulus_filter.value) {
            showRow = false
        }
        if (tensile_strength_filter.value && tensile_strength_data.innerText != tensile_strength_filter.value) {
            showRow = false
        }
        if (resin_matrix_filter.value && resin_matrix_data.innerText != resin_matrix_filter.value) {
            showRow = false
        }
        if (carbon_fiber_processing_filter.value && carbon_fiber_processing_data.innerText != carbon_fiber_processing_filter.value) {
            showRow = false
        }

        // This will determine whether we show or hide the data we ask for. 
        if (showRow) {
            row.classList.remove("hide")
        } else {
            row.classList.add("hide")
        }
    }
}

function handleFilterChangePP() {

    let tg_filter = document.getElementById('tg_filter')
    let cure_temp_filter = document.getElementById('cure_temp_filter')
    let prepreg_processing_filter = document.getElementById('prepreg_processing_filter')
    let omit_filter = document.getElementById('omit_filter')       
    let resin_type_filter = document.getElementById('resin_type_filter')         
    let ppRows = document.getElementsByClassName('pp_row')

    for (let row of ppRows) {
        let tg_data = row.getElementsByClassName('tg')[0]
        let cure_temp_data = row.getElementsByClassName('cure_temp')[0]
        let prepreg_processing_data = row.getElementsByClassName('prepreg_processing')[0]
        let omit_data = row.getElementsByClassName('omit')[0]
        let resin_type_data = row.getElementsByClassName('resin_type')[0]
        let showRow = true
        
        if (tg_filter.value && tg_data.innerText != tg_filter.value) {
            showRow = false
        }
        if (cure_temp_filter.value && cure_temp_data.innerText != cure_temp_filter.value) {
            showRow = false
        }
        if (prepreg_processing_filter.value && prepreg_processing_data.innerText != prepreg_processing_filter.value) {
            showRow = false
        }
        if (omit_filter.value && omit_data.innerText != omit_filter.value) {
            showRow = false
        }
        if (resin_type_filter.value && resin_type_data.innerText != resin_type_filter.value) {
            showRow = false
        }

        // This will determine whether we show or hide the data we ask for. 
        if (showRow) {
            row.classList.remove("hide")
        } else {
            row.classList.add("hide")
        }
    }
}