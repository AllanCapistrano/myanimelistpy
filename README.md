[![Documentation Status](https://readthedocs.org/projects/myanimelistpy/badge/?version=latest)](https://myanimelistpy.readthedocs.io/en/latest/?badge=latest)
[![Codecov](https://img.shields.io/codecov/c/gh/AllanCapistrano/myanimelistpy?logo=codecov)](https://app.codecov.io/gh/AllanCapistrano/myanimelistpy)
# myanimelistpy

<p align="center">
  <img src="https://github.com/AllanCapistrano/myanimelistpy/blob/main/images/myanimelistpy-logo-rounded.png?raw=true" alt="myanimelistpy icon" width="180px" height="180px">
</p>
<h3 align="center">A library to use the MyAnimeList API more easily.</h3>

## Installing
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

## Examples

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
        limit      = 2
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

## Creator ##

| [![Allan Capistrano](https://github.com/AllanCapistrano.png?size=100)](https://github.com/AllanCapistrano) |
| -----------------------------------------------------------------------------------------------------------|
| [Allan Capistrano](https://github.com/AllanCapistrano)                                                     |

## Support ##

**Please star this repository if this project is useful or helped you.**

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/allancapistrano)

---

## License ##
[GPL-3.0 License](https://github.com/AllanCapistrano/myanimelistpy/blob/main/License)
