# Importing all the necessary modules
import streamlit as st
import pandas as pd
import datetime
import plotly.graph_objects as go
from datetime import date
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import xarray as xr
import folium
from streamlit_folium import st_folium
import math

# Defining the function of netCDF file loading based on the datetime (string
def open_dataset_with_fallback(url_list):
    """
    Tries to open a dataset from a list of URLs.

    Args:
        url_list: A list of URLs to try.

    Returns:
        An xarray Dataset, or None if all URLs fail.
    """

    for url in url_list:
        try:
            ds = xr.open_dataset(url)
            return ds
        except Exception as e:
            print(f"Error opening {url}: {e}")
            continue

    return None

# Get the necessary datetimes of today, yesterday, and tomorrow
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=2)

# Calculate necessary datetime's strings
open_date_year = yesterday.strftime("%Y")
open_date_month = yesterday.strftime("%m")
open_date_day = yesterday.strftime("%d")
select_date_i = today.strftime("%Y-%m-%d")
select_date_f = tomorrow.strftime("%Y-%m-%d")

# List of CAWO OpenDAP url name
cawo_url_name_1 = 'https://renderofs:AksesTerbatas2303!!!@maritim.bmkg.go.id/opendap/inaCawo/'+open_date_year+'/'+open_date_month+'/InaCAWOAtmos_'+open_date_year+open_date_month+open_date_day+'_1800.nc'
cawo_url_name_2 = 'https://renderofs:AksesTerbatas2303!!!@maritim.bmkg.go.id/opendap/inaCawo/'+open_date_year+'/'+open_date_month+'/InaCAWOAtmos_'+open_date_year+open_date_month+open_date_day+'_1200.nc'
cawo_url_name_3 = 'https://renderofs:AksesTerbatas2303!!!@maritim.bmkg.go.id/opendap/inaCawo/'+open_date_year+'/'+open_date_month+'/InaCAWOAtmos_'+open_date_year+open_date_month+open_date_day+'_0600.nc'
cawo_url_name_4 = 'https://renderofs:AksesTerbatas2303!!!@maritim.bmkg.go.id/opendap/inaCawo/'+open_date_year+'/'+open_date_month+'/InaCAWOAtmos_'+open_date_year+open_date_month+open_date_day+'_0000.nc'

url_list = [
    cawo_url_name_1,
    cawo_url_name_2,
    cawo_url_name_3,
    cawo_url_name_4
]

# Load the CAWO netCDF filename
ds = open_dataset_with_fallback(url_list)
dset_temp = ds

# Classify the dataset into several tables based on the port coordinates
# 'Pelabuhan Ambarita'
df_1 = pd.DataFrame()

u = dset_temp.uwnd.sel(lat=2.682399, lon=98.832537, method='nearest')
v = dset_temp.vwnd.sel(lat=2.682399, lon=98.832537, method='nearest')
u = u.to_dataframe()
v = v.to_dataframe()

df_1 = u
df_1['vwnd'] = v['vwnd']

df_1['wind'] = (df_1['vwnd']**2 + df_1['vwnd']**2)**0.5

#df['hs'] = ((df['wind']**2)(0.283(np.tanh(0.0125*(((9.8*65)/(df['wind']**2)))))**0.42))/9.8

#df_1['hs'] = 2.482*(0.01)*(df_1['wind'])*(65**0.5)
df_1['hs'] = 1.616*(0.01)*(df_1['wind'])*(65**0.5)

#df['hs_full'] = 2.482*(0.01)*(df['wind']**2)
df_1 = df_1[df_1.index > select_date_i]
df_1 = df_1[df_1.index < select_date_f]

# 'Pelabuhan Nainggolan'
df_2 = pd.DataFrame()

u = dset_temp.uwnd.sel(lat=2.434639, lon=98.898055, method='nearest')
v = dset_temp.vwnd.sel(lat=2.434639, lon=98.898055, method='nearest')
u = u.to_dataframe()
v = v.to_dataframe()

df_2 = u
df_2['vwnd'] = v['vwnd']

df_2['wind'] = (df_2['vwnd']**2 + df_2['vwnd']**2)**0.5

df_2['hs'] = 2.482*(0.01)*(df_2['wind'])*(65**0.5)

df_2 = df_2[df_2.index > select_date_i]
df_2 = df_2[df_2.index < select_date_f]

# 'Pelabuhan Pardomuan'
df_3 = pd.DataFrame()

u = dset_temp.uwnd.sel(lat=2.601156, lon=98.701938, method='nearest')
v = dset_temp.vwnd.sel(lat=2.601156, lon=98.701938, method='nearest')
u = u.to_dataframe()
v = v.to_dataframe()

df_3 = u
df_3['vwnd'] = v['vwnd']

df_3['wind'] = (df_3['vwnd']**2 + df_3['vwnd']**2)**0.5

df_3['hs'] = 2.482*(0.01)*(df_3['wind'])*(65**0.5)

df_3 = df_3[df_3.index > select_date_i]
df_3 = df_3[df_3.index < select_date_f]

# 'Pelabuhan Simanindo'
df_4 = pd.DataFrame()

u = dset_temp.uwnd.sel(lat=2.753853, lon=98.745361, method='nearest')
v = dset_temp.vwnd.sel(lat=2.753853, lon=98.745361, method='nearest')
u = u.to_dataframe()
v = v.to_dataframe()

df_4 = u
df_4['vwnd'] = v['vwnd']

df_4['wind'] = (df_4['vwnd']**2 + df_4['vwnd']**2)**0.5

df_4['hs'] = 2.482*(0.01)*(df_4['wind'])*(65**0.5)

df_4 = df_4[df_4.index > select_date_i]
df_4 = df_4[df_4.index < select_date_f]

# 'Pelabuhan Ajibata'
df_5 = pd.DataFrame()

u = dset_temp.uwnd.sel(lat=2.659434, lon=98.934624, method='nearest')
v = dset_temp.vwnd.sel(lat=2.659434, lon=98.934624, method='nearest')
u = u.to_dataframe()
v = v.to_dataframe()

df_5 = u
df_5['vwnd'] = v['vwnd']

df_5['wind'] = (df_5['vwnd']**2 + df_5['vwnd']**2)**0.5

df_5['hs'] = 2.482*(0.01)*(df_5['wind'])*(65**0.5)

df_5 = df_5[df_5.index > select_date_i]
df_5 = df_5[df_5.index < select_date_f]

# 'Pelabuhan Balige'
df_6 = pd.DataFrame()

u = dset_temp.uwnd.sel(lat=2.337431, lon=99.062806, method='nearest')
v = dset_temp.vwnd.sel(lat=2.337431, lon=99.062806, method='nearest')
u = u.to_dataframe()
v = v.to_dataframe()

df_6 = u
df_6['vwnd'] = v['vwnd']

df_6['wind'] = (df_6['vwnd']**2 + df_6['vwnd']**2)**0.5

#df['hs'] = ((df['wind']**2)(0.283(np.tanh(0.0125*(((9.8*65)/(df['wind']**2)))))**0.42))/9.8
df_6['hs'] = 2.482*(0.01)*(df_6['wind'])*(65**0.5)
#df['hs_full'] = 2.482*(0.01)*(df['wind']**2)
df_6 = df_6[df_6.index > select_date_i]
df_6 = df_6[df_6.index < select_date_f]

# 'Pelabuhan Tigaras'
df_7 = pd.DataFrame()

u = dset_temp.uwnd.sel(lat=2.327367, lon=98.821722, method='nearest')
v = dset_temp.vwnd.sel(lat=2.327367, lon=98.821722, method='nearest')
u = u.to_dataframe()
v = v.to_dataframe()

df_7 = u
df_7['vwnd'] = v['vwnd']

df_7['wind'] = (df_7['vwnd']**2 + df_7['vwnd']**2)**0.5

df_7['hs'] = 2.482*(0.01)*(df_7['wind'])*(65**0.5)

df_7 = df_7[df_7.index > select_date_i]
df_7 = df_7[df_7.index < select_date_f]

# 'Pelabuhan Muara'
df_8 = pd.DataFrame()

u = dset_temp.uwnd.sel(lat=2.338063, lon=98.903850, method='nearest')
v = dset_temp.vwnd.sel(lat=2.338063, lon=98.903850, method='nearest')
u = u.to_dataframe()
v = v.to_dataframe()

df_8 = u
df_8['vwnd'] = v['vwnd']

df_8['wind'] = (df_8['vwnd']**2 + df_8['vwnd']**2)**0.5

df_8['hs'] = 2.482*(0.01)*(df_8['wind'])*(65**0.5)

df_8 = df_8[df_8.index > select_date_i]
df_8 = df_8[df_8.index < select_date_f]

# 'Pelabuhan Silalahi'
df_9 = pd.DataFrame()

u = dset_temp.uwnd.sel(lat=2.849440, lon=98.526642, method='nearest')
v = dset_temp.vwnd.sel(lat=2.849440, lon=98.526642, method='nearest')
u = u.to_dataframe()
v = v.to_dataframe()

df_9 = u
df_9['vwnd'] = v['vwnd']

df_9['wind'] = (df_9['vwnd']**2 + df_9['vwnd']**2)**0.5

df_9['hs'] = 2.482*(0.01)*(df_9['wind'])*(65**0.5)

df_9 = df_9[df_9.index > select_date_i]
df_9 = df_9[df_9.index < select_date_f]

# 'Pelabuhan Tongging'
df_10 = pd.DataFrame()

u = dset_temp.uwnd.sel(lat=2.896527, lon=98.528209, method='nearest')
v = dset_temp.vwnd.sel(lat=2.896527, lon=98.528209, method='nearest')
u = u.to_dataframe()
v = v.to_dataframe()

df_10 = u
df_10['vwnd'] = v['vwnd']

df_10['wind'] = (df_10['vwnd']**2 + df_10['vwnd']**2)**0.5

df_10['hs'] = 2.482*(0.01)*(df_10['wind'])*(65**0.5)

df_10 = df_10[df_10.index > select_date_i]
df_10 = df_10[df_10.index < select_date_f]

# 'Pelabuhan Baktiraja'
df_11 = pd.DataFrame()

u = dset_temp.uwnd.sel(lat=2.327345, lon=98.821725, method='nearest')
v = dset_temp.vwnd.sel(lat=2.327345, lon=98.821725, method='nearest')
u = u.to_dataframe()
v = v.to_dataframe()

df_11 = u
df_11['vwnd'] = v['vwnd']

df_11['wind'] = (df_11['vwnd']**2 + df_11['vwnd']**2)**0.5

df_11['hs'] = 2.482*(0.01)*(df_11['wind'])*(65**0.5)

df_11 = df_11[df_11.index > select_date_i]
df_11 = df_11[df_11.index < select_date_f]

# Image URL of the icon and image title
icon_url = "https://upload.wikimedia.org/wikipedia/commons/1/12/Logo_BMKG_%282010%29.png"
st.set_page_config(page_title="Prakiraan Tinggi Gelombang Danau Toba", page_icon=icon_url, layout="wide")

margins_css = """
<style>
  .appview-container .main .block-container {
    padding-top: 1rem;
  }
</style>
"""


st.markdown(margins_css, unsafe_allow_html=True)

# Display the image title and title itself
col1, col2 = st.columns([2, 11])
with col1:
    st.write(' ')
    st.write(' ')
    st.image(icon_url , width=80)
    #st.image(icon_url, width=80, style={"margin-top": "20px"})
with col2:
    st.write(' ')
    st.write(' ')
    st.title("Prakiraan Tinggi Gelombang Danau Toba")
    #st.write("Danau Toba")

col1, col2 = st.columns([10, 38])

with col1:
    # Choosing the start and end time interface
    locations = ['Pelabuhan Ambarita', 'Pelabuhan Nainggolan', 'Pelabuhan Pardomuan', 'Pelabuhan Simanindo', 'Pelabuhan Ajibata', 'Pelabuhan Balige', 'Pelabuhan Tigaras', 'Pelabuhan Muara', 'Pelabuhan Silalahi', 'Pelabuhan Tongging', 'Pelabuhan Baktiraja']
    selected_location = st.selectbox('Pilih lokasi:', locations)
    
    # Display or use the selected date
    st.write("Lokasi:", selected_location)

    # Conditions to pick the correct dataframe match with selected location
    if selected_location == 'Pelabuhan Ambarita':
        series_to_plot = df_1
    elif selected_location == 'Pelabuhan Nainggolan':
        series_to_plot = df_2
    elif selected_location == 'Pelabuhan Pardomuan':
        series_to_plot = df_3
    elif selected_location == 'Pelabuhan Simanindo':
        series_to_plot = df_4    
    elif selected_location == 'Pelabuhan Ajibata':
        series_to_plot = df_5 
    elif selected_location == 'Pelabuhan Balige':
        series_to_plot = df_6 
    elif selected_location == 'Pelabuhan Tigaras':
        series_to_plot = df_7 
    elif selected_location == 'Pelabuhan Muara':
        series_to_plot = df_8 
    elif selected_location == 'Pelabuhan Silalahi':
        series_to_plot = df_9 
    elif selected_location == 'Pelabuhan Tongging':
        series_to_plot = df_10 
    else:
        series_to_plot = df_11
        
    # Select the date only for 2 days    
    series_to_plot = series_to_plot[series_to_plot.index > select_date_i]
    series_to_plot = series_to_plot[series_to_plot.index < select_date_f]
    start_date = series_to_plot.index[0]
    end_date = series_to_plot.index[-1]

    # Plot the coordinate of the selected dataframe to folium map
    latitude_plot = series_to_plot['lat'].iloc[0]
    longitude_plot = series_to_plot['lon'].iloc[0]

    # Buat peta Folium
    m = folium.Map(location=[latitude_plot, longitude_plot], zoom_start=12)

    # Tambahkan marker atau fitur lainnya
    folium.Marker([latitude_plot, longitude_plot], popup=selected_location).add_to(m)

    # Simpan peta ke dalam buffer
    #from io import BytesIO
    #m.save("map.html")
    
    # Membaca peta dari file HTML dan menampilkannya sebagai gambar
    #img = Image.open("map.html")  # Gunakan peta sebagai gambar
    #st.image(img, caption=selected_location, use_column_width=True)
    
    # Show the folium map on column one
    st_folium(m, width=200, height=300)

    st.write("Tanggal awal:", start_date)
    st.write("Tanggal akhir:", end_date)
    
    
# Assuming your dataframe is called 'df' and the index is datetime
df_tabel = pd.DataFrame()

# Creating the table for the table at the bottom of graph
waktu = [ '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',  '21',  '22',  '23', ]

#series_to_plot = series_to_plot[series_to_plot.index > select_date_i]
#series_to_plot = series_to_plot[series_to_plot.index < select_date_f]
series_to_plot_ok = series_to_plot['hs']

for jam in waktu:
    jam = jam + ':00:00'
    df_filtered = series_to_plot_ok[series_to_plot_ok.index.strftime('%H:%M:%S') == jam]
    df_filtered = df_filtered.reset_index(drop=True)
    df_tabel = pd.concat([df_tabel, df_filtered], axis=1, ignore_index=True)
#df_tabel
increment = pd.Timedelta(days=1)  # Increment of 1 hour
timestamps = pd.date_range(start_date, end_date, freq='D')
#timestamps = pd.date_range(start_date, end_date, freq='D', format='%d-%m-%Y')
df_tabel['tanggal_jam'] = timestamps
df_tabel = df_tabel.set_index('tanggal_jam')
df_tabel = df_tabel.round(1)  
    
with col2:
    st.subheader('Tinggi Gelombang '+selected_location+ " (meter)")
    #st.write("This text appears in the second column.")
    #st.title('Pasang Surut '+selected_location)
    #fig = st.line_chart(series_to_plot)
    
    #fig = go.Figure()

    # Add the first trace
    #fig.add_trace(go.Scatter(x=series_to_plot.index, y=series_to_plot['hs'], name='Wave height (m)'))

    # Add the second trace with a secondary y-axis
    #fig.add_trace(go.Scatter(x=series_to_plot.index, y=series_to_plot['wind'], name='Wind speed (m/s)', yaxis='y2'))

    # Update layout for secondary y-axis
    #fig.update_layout(yaxis2=dict(title='Wind speed', overlaying='y', side='right'))

    # Display the plot in Streamlit
    #st.plotly_chart(fig)
    
    # Build the graph plot
    fig = st.line_chart(series_to_plot_ok)
    ##fig = st.line_chart(series_to_plot['wind'])

    st.dataframe(df_tabel)
    #st.dataframe(series_to_plot)
