# How to embed Google Slides in a cell

- Figure out the `deck_id` looking at the URL. This should be the string before `/embed` in the URL.
- Run the cell below which defines the function to embed GSlide using `iframe`
- Then invoke the function with the `deck_id` and the `slide_number` in any cell you want to embed the deck. The iframe is initialized to start from the `slide_number` you specify. Example:

`embedGoogleSlides('1d3ck1dfromth3url', '1')`
