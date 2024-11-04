# 👩‍🎨 Virtual Exhibition Generator🖼️ 

### Overview

The Virtual Exhibition Generator is an app designed to create personalised digital art exhibitions. By selecting art categories, users can view curated artwork images and listen to music recommendations that align with the selected art theme.



### Features

- **Artwork Display**: Connects to the Art Institute of Chicago API to fetch and display images for selected categories, creating a virtual art exhibition.

- **Music Curation**: Integrates with Spotify’s API to provide genre-based music recommendations that match the art categories chosen by the user.

- **Automated Playlist Creation**: Compiles a Spotify playlist based on selected categories, allowing users to enjoy a tailored audio experience while viewing the exhibition.

  

### Installation

1. **Clone the Repository**:

   ```
   git clone <repository-url>
   cd Virtual-Exhibition-Generator
   ```

2. **Install Required Packages**:

   ```
   pip install -r requirements.txt
   ```

3. **API Keys**:

   **Spotify**: Create a `spotify_keys.json` file with the following structure, and insert your API keys:

   ```
   {
     "client_id": "your_spotify_client_id",
     "client_secret": "your_spotify_client_secret",
     "redirect": "your_redirect_url",
     "username": "your_spotify_username"
   }
   ```

   **Art Institute of Chicago API**: This API does not require authentication, so no additional setup is needed for this.

   

### Usage

1. **Selecting Categories**: Modify `selected_categories` in the main function to include the art categories you want to explore, e.g., `"Modern Art"`, `"Photography"`.

2. **Run the Notebook**: Execute each cell in order, ensuring data is loaded and APIs are connected.

3. **View the Exhibition**: The notebook will display images based on selected categories and provide a Spotify playlist link.

   

### Example Code

```
selected_categories = ["Modern Art", "Contemporary Art"]
create_virtual_exhibition(selected_categories, num_images=5, num_songs=5)
```



### Troubleshooting

- **Image Not Displaying**: Verify that `image_id` is correctly used to construct the image URL.
- **API Authentication Errors**: Ensure your Spotify credentials are correctly set in `spotify_keys.json` and that the necessary scopes are included.
- 

### Future Enhancements

- Add more art genres to the music mapping.
- Integrate additional museum APIs for a broader range of artworks.