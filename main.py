import os
import requests
import zipfile
import subprocess
import tkinter as tk
from tkinter import Toplevel, messagebox
from PIL import Image, ImageTk
import io
import webbrowser


def main():
    root = tk.Tk()
    root.title("Steam Game Downgrader")
    root.geometry("800x600")
    root.configure(bg='#000014')

    # Define and place the label
    label = tk.Label(root, text="Enter the Steam App ID:", font=("Arial", 12), bg='#000014', fg='#dcddf7')
    label.pack(pady=(20, 10))

    # Define and place the entry
    app_id_entry = tk.Entry(root, font=("Arial", 12), bg='#33334d', fg='white', borderwidth=2, relief="flat")
    app_id_entry.pack(pady=(10, 20))

    # Define and place the button
    find_button = tk.Button(root, text="Find Versions", font=("Arial", 12), bg='#4b4b65', fg='#dcddf7',
                            activebackground='#4b4b65', activeforeground='#ffffff', relief="flat",
                            command=lambda: find_game_versions(app_id_entry.get(), root))
    find_button.pack(pady=(0, 20))

    root.mainloop()


def find_game_versions(app_id, root):
    url = f"https://store.steampowered.com/api/appdetails?appids={app_id}"
    response = requests.get(url)
    data = response.json()

    if data[str(app_id)]['success']:
        game_name = data[str(app_id)]['data']['name']
        game_image_url = f"https://cdn.akamai.steamstatic.com/steam/apps/{app_id}/header.jpg"

        image_response = requests.get(game_image_url)
        image_data = Image.open(io.BytesIO(image_response.content))
        image = ImageTk.PhotoImage(image_data)

        new_window = Toplevel(root)
        new_window.title(game_name)
        new_window.geometry("500x500")
        new_window.configure(bg='#000014')

        image_label = tk.Label(new_window, image=image)
        image_label.image = image
        image_label.pack(pady=(10, 10))

        name_label = tk.Label(new_window, text=game_name, font=("Arial", 16), bg='#000014', fg='#dcddf7')
        name_label.pack(pady=(0, 20))

        continue_button = tk.Button(new_window, text="Continue", font=("Arial", 12), bg='#4b4b65', fg='#dcddf7',
                                    activebackground='#4b4b65', activeforeground='#ffffff', relief="flat",
                                    command=lambda: open_depots_page(app_id))
        continue_button.pack(pady=(20, 0))
    else:
        messagebox.showerror("Error", "Oops! Could not find game!")


def open_depot_window(app_id):
    depot_window = Toplevel()
    depot_window.title("Enter Depot ID")
    depot_window.geometry("300x200")
    depot_window.configure(bg='#000014')

    label = tk.Label(depot_window, text="Enter the Depot ID:", font=("Arial", 12), bg='#000014', fg='#dcddf7')
    label.pack(pady=(20, 10))

    depot_entry = tk.Entry(depot_window, font=("Arial", 12), bg='#33334d', fg='white', borderwidth=2, relief="flat")
    depot_entry.pack(pady=(10, 20))

    confirm_button = tk.Button(depot_window, text="Confirm", font=("Arial", 12), bg='#4b4b65', fg='#dcddf7',
                               activebackground='#4b4b65', activeforeground='#ffffff', relief="flat",
                               command=lambda: retrieve_depot(depot_entry.get(), depot_window, app_id))
    confirm_button.pack(pady=(0, 20))


def retrieve_depot(depot_id, window, app_id):
    print(f"Depot ID is: {depot_id}")
    window.destroy()
    open_manifest_window(depot_id, app_id)


def open_manifest_window(depot_id, app_id):
    manifest_window = Toplevel()
    manifest_window.title("Enter Manifest ID")
    manifest_window.geometry("300x200")
    manifest_window.configure(bg='#000014')

    label = tk.Label(manifest_window, text=f"Depot {depot_id}: Enter the Manifest ID:", font=("Arial", 12),
                     bg='#000014', fg='#dcddf7')
    label.pack(pady=(20, 10))

    manifest_entry = tk.Entry(manifest_window, font=("Arial", 12), bg='#33334d', fg='white', borderwidth=2,
                              relief="flat")
    manifest_entry.pack(pady=(10, 20))

    confirm_button = tk.Button(manifest_window, text="Confirm", font=("Arial", 12), bg='#4b4b65', fg='#dcddf7',
                               activebackground='#4b4b65', activeforeground='#ffffff', relief="flat",
                               command=lambda: retrieve_manifest(manifest_entry.get(), manifest_window, depot_id, app_id))
    confirm_button.pack(pady=(0, 20))


def retrieve_manifest(manifest_id, window, depot_id, app_id):
    print(f"Manifest ID for Depot {depot_id} is: {manifest_id}")
    window.destroy()
    install_steamcmd_if_needed(app_id, depot_id, manifest_id)


def install_steamcmd_if_needed(app_id, depot_id, manifest_id):
    if not os.path.exists('./steamcmd/'):
        messagebox.showinfo("Installation", "steamcmd is not found. It will be installed.")
        url = "https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip"
        r = requests.get(url)

        with open("steamcmd.zip", "wb") as code:
            code.write(r.content)

        with zipfile.ZipFile("steamcmd.zip", "r") as zip_ref:
            zip_ref.extractall("./steamcmd/")

        os.remove("steamcmd.zip")

    download_old_version(app_id, depot_id, manifest_id)


def download_old_version(app_id, depot_id, manifest_id):
    command = f'./steamcmd/steamcmd.exe +login anonymous +download_depot {app_id} {depot_id} {manifest_id} +quit'
    process = subprocess.Popen(command, shell=True)
    process.wait()  # Wait for the process to complete

    messagebox.showinfo("Success", "Your old version has been installed!!!")


def open_depots_page(app_id):
    url = f"https://steamdb.info/app/{app_id}/depots/"
    webbrowser.open(url, new=2)
    open_depot_window(app_id)


if __name__ == "__main__":
    main()
