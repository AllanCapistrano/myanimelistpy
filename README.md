# myanimelistpy

<p align="center">
  <img src="https://github.com/AllanCapistrano/myanimelistpy/blob/main/images/myanimelistpy-logo-rounded.png" alt="myanimelistpy icon" width="180px" height="180px">
</p>
<h3 align="center">A library to use the MyAnimeList API more easily.</h3>

## ⚙️ Installing
```powershell
pip install myanimelistpy
```

or

```powershell
# Linux/macOS
python3 -m pip install -U myanimelistpy

# Windows
py -m pip install -U myanimelistpy
```

---

## ✍️ Examples

### Anime List
<details>
<summary>Basic example:</summary>

```python
from myanimelistpy.myanimelist import MyAnimeList

CLIENT_ID = "YOUR_MY_ANIME_LIST_CLIENT_ID"

if __name__ == "__main__":
    my_anime_list = MyAnimeList(client_id=CLIENT_ID)

    anime_list = my_anime_list.getAnimeList(
        anime_name = "Hunter x Hunter",
        limit      = 4
    )

    for anime in anime_list:
        print(f"Id: {anime.getId()}")
        print(f"Title: {anime.getTitle()}")
        print(f"Main Picture (medium): {anime.getMainPicture().getMedium()}\n")
```

#### Output
```powershell
Id: 11061
Title: Hunter x Hunter (2011)
Main Picture (medium): https://api-cdn.myanimelist.net/images/anime/1337/99013.jpg

Id: 136
Title: Hunter x Hunter
Main Picture (medium): https://api-cdn.myanimelist.net/images/anime/8/19473.jpg
```
</details>

<details>
<summary>Request with fields:</summary>

```python
from myanimelistpy.myanimelist import MyAnimeList

CLIENT_ID = "YOUR_MY_ANIME_LIST_CLIENT_ID"

if __name__ == "__main__":
    my_anime_list = MyAnimeList(client_id=CLIENT_ID)

    anime_list = my_anime_list.getAnimeList(
        anime_name = "Hunter x Hunter",
        limit      = 2,
        fields     = ["rank", "status"]
    )

    for anime in anime_list:
        print(f"Id: {anime.getId()}")
        print(f"Title: {anime.getTitle()}")
        print(f"Main Picture (medium): {anime.getMainPicture().getMedium()}")
        print(f"Rank: {anime.getRank()}")
        print(f"Status: {anime.getStatus()}\n")
```

#### Output
```powershell
Id: 11061
Title: Hunter x Hunter (2011)
Main Picture (medium): https://api-cdn.myanimelist.net/images/anime/1337/99013.jpg
Rank: 9
Status: Finished airing

Id: 136
Title: Hunter x Hunter
Main Picture (medium): https://api-cdn.myanimelist.net/images/anime/8/19473.jpg   
Rank: 165
Status: Finished airing
```
</details>

---

## 👨‍💻 Creator ##

| [![Allan Capistrano](https://github.com/AllanCapistrano.png?size=100)](https://github.com/AllanCapistrano) |
| -----------------------------------------------------------------------------------------------------------|
| [Allan Capistrano](https://github.com/AllanCapistrano)                                                     |

<p>
    <h3>How to find me:</h3>
    <a href="https://github.com/AllanCapistrano">
        <img src="https://github.com/AllanCapistrano/AllanCapistrano/blob/master/assets/github-square-brands.png" alt="Github icon" width="5%">
    </a>
    &nbsp
    <a href="https://www.linkedin.com/in/allancapistrano/">
        <img src="https://github.com/AllanCapistrano/AllanCapistrano/blob/master/assets/linkedin-brands.png" alt="Linkedin icon" width="5%">
    </a> 
    &nbsp
    <a href="https://mail.google.com/mail/u/0/?view=cm&fs=1&tf=1&source=mailto&to=asantos@ecomp.uefs.br">
        <img src="https://github.com/AllanCapistrano/AllanCapistrano/blob/master/assets/envelope-square-solid.png" alt="Email icon" width="5%">
    </a>
</p>

---

## 🙏 Support ##

**Please ⭐️ this repository if this project is useful or helped you.**

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/allancapistrano)

---

## ⚖️ License ##
[GPL-3.0 License](https://github.com/AllanCapistrano/myanimelistpy/blob/main/License)
