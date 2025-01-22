# Vikingarr
Inspired by the adventurous spirit of the Vikings, Vikingarr helps you ethically "raid" the digital seas of music, bringing your favorites home to your NAS and creating auto-generated playlists in Plex.

Here’s a concise and engaging project description for Vikingarr:

Vikingarr: Pillage the Digital Seas, Bring Your Music Home
Vikingarr is an open-source automation tool designed to seamlessly retrieve your Spotify favorites, download tracks from legal sources, enrich them with metadata, and organize them into a Plex library.

Inspired by the adventurous spirit of the Vikings, Vikingarr helps you ethically "raid" the digital seas of music, bringing your favorites home to your NAS and creating auto-generated playlists in Plex.

Whether you're curating your personal Hall of Music or simply want an effortless way to manage your favorites, Vikingarr ensures a smooth and customizable experience for music enthusiasts.

Features:

Automate fetching Spotify favorites and playlists.
Download tracks from ethical, open-source tools.
Add metadata like album art and artist info.
Organize and store music on a NAS with customizable structures.
Integrate with Plex Media Server for easy playback and playlist management.
Open-source and community-driven—expand and adapt it to your needs.
Join us in pillaging the digital seas and building your ultimate music library. 🌊 🎵 🛡️

vikingarr/
├── README.md               # Overview, setup instructions, and usage guide
├── LICENSE                 # License for the project (e.g., MIT, GPL)
├── requirements.txt        # Python dependencies
├── config/
│   ├── spotify_credentials.json   # Spotify API keys and settings
│   ├── plex_credentials.json      # Plex API token and server settings
│   ├── vikingarr_settings.yaml    # General configuration (e.g., NAS paths, default formats)
├── scripts/
│   ├── fetch_spotify_favorites.py # Retrieve favorites/playlists from Spotify
│   ├── download_tracks.py         # Download tracks using YouTube or another source
│   ├── add_metadata.py            # Enhance tracks with metadata and album art
│   ├── organize_files.py          # Move files to NAS and organize them
│   ├── update_plex_library.py     # Trigger Plex library refresh
│   ├── create_plex_playlist.py    # Create playlists in Plex
│   ├── run_all.sh                 # Main script to run the full Vikingarr process
├── tests/
│   ├── test_fetch_spotify.py      # Test Spotify API integration
│   ├── test_download_tracks.py    # Test download functionality
│   ├── test_metadata.py           # Test metadata tagging
│   ├── test_plex_integration.py   # Test Plex API integration
├── docs/
│   ├── CONTRIBUTING.md            # Guide for contributing to the project
│   ├── CHANGELOG.md               # Version history and changes
│   ├── setup_guide.md             # Detailed setup instructions
│   ├── api_docs.md                # Documentation for the APIs used
│   ├── examples/
│   │   ├── sample_playlist.json   # Example Spotify playlist data
│   │   ├── sample_metadata.yaml   # Example metadata configuration
├── assets/
│   ├── logo.png                   # Vikingarr logo
│   ├── screenshots/               # Screenshots of the app/tool
│   ├── icons/                     # Any custom icons or visuals
├── logs/
│   ├── vikingarr.log              # Logs for debugging and tracking
│   ├── error.log                  # Separate error log
└── .github/
    ├── ISSUE_TEMPLATE.md          # Template for reporting issues
    ├── PULL_REQUEST_TEMPLATE.md   # Template for pull requests
