# Databricks notebook source
# MAGIC %md ##How to embed Google Slides in a cell
# MAGIC 
# MAGIC - Figure out the `deck_id` looking at the URL. This should be the string before `/embed` in the URL.
# MAGIC - Run the cell below which defines the function to embed GSlide using `iframe`
# MAGIC - Then invoke the function with the `deck_id` and the `slide_number` in any cell you want to embed the deck. The iframe is initialized to start from the `slide_number` you specify. Example:
# MAGIC 
# MAGIC `embedGoogleSlides('1d3ck1dfromth3url', '1')`

# COMMAND ----------

def embedGoogleSlides(deck_id, slide_number=1):
  
  displayHTML(f'''

  <iframe
    src="https://docs.google.com/presentation/d/{deck_id}/embed?slide={slide_number}&rm=minimal"
    frameborder="0"
    width="100%"
    height="700"
  ></iframe>

  ''')

# COMMAND ----------

embedGoogleSlides('1cCXQ1MWPjwZ3eKAvwRhLavBBw18h2YhXJhtn1cv4GTQ')

# COMMAND ----------

# MAGIC %md 
# MAGIC #Do Something Else Here

# COMMAND ----------

# Embed slides again
embedGoogleSlides('1cCXQ1MWPjwZ3eKAvwRhLavBBw18h2YhXJhtn1cv4GTQ', 7)

# COMMAND ----------


