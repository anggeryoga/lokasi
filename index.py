def create_google_maps_link(latitude, longitude):
    """Membuat link Google Maps berdasarkan latitude dan longitude."""
    return f"https://www.google.com/maps?q={latitude},{longitude}"

def main():
    print("Masukkan koordinat lokasi:")
    
    # Meminta input dari pengguna
    latitude = input("Latitude: ")
    longitude = input("Longitude: ")

    # Membuat link Google Maps
    link = create_google_maps_link(latitude, longitude)
    
    print(f"Link Google Maps: {link}")

if __name__ == "__main__":
    main()
