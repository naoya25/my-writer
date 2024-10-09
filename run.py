from PIL import Image
import string


text = """
learn fiber optics with senko welcome to the connected world every day roughly  2.5 quintillion bytes of data voice and video are transmitted all over the world  enabling our modern life in order to transport all of this information billions of kilometers  of fiber are deployed around the world like the artery of global telecommunication networks  this is due to its advantages over copper cables such as its greater bandwidth  immunity to interference ability to reach longer distances overall better reliability and it is
also thinner and lighter let's learn more about the optical fiber and how it is made basically  an optical fiber is a very thin strand of glass about the same diameter as a strand of hair pretty  impressive isn't it to the naked eye all optical fibers may look the same however that's not the  case there are many different types of optical fibers each with their own specific application  some examples are the single mode fiber multi-mode fiber dispersion shifted single  mode fiber non-zero dispersion shifted single mode fiber and bin insensitive single mode fiber
all of them have a similar basic structure which is a core in the middle and a cladding around it  so how is information being transmitted through something so small and fragile as glass  the fiber core and cladding have different indexes of refraction this difference keeps the light from  escaping the core through a phenomenon called total internal reflection or tir generally there  are two types of optical fiber namely the single mode fiber and the multimode fiber they have  different core sizes and index of refraction which make light behave differently inside of the core
single mode fibers and multimode fibers can further be broken down to different categories  the single mode fiber can be categorized under as os1 and os2 while both have the same physical  dimensions os1 fiber has a higher attenuation per kilometer of fiber and is only suitable  for indoor use while os2 fiber is suitable for indoor and outdoor deployment there are five  types of multimode fibers which are om1 om2 om3 om4 and the om5 with om1 being the oldest  standard and om5 being the latest they have different core diameter sizes and can commonly
be identified based on the standard jacket color defined by various standard bodies each type of  multimode fiber has a minimum modal bandwidth with the latest multi-mode standard om-5 being  able to support higher bandwidth transmission for longer distances compared to the earlier standards  optical fiber starts as a hollow tube of glass gases that contain silicon germanium  and many other chemicals are injected through the rotating tube the glass tube is then heated by an  oxyhydrogen burner that traverses its length this creates soot deposition on the inner wall of the
glass tube further heating at higher temperatures during rotation causes it to collapse uniformly  which results in the production of a fiber preform a fiber preform is a rod of pure glass  with a refractive index identical to that of the desired fiber the fiber preform is then mounted at  the top of a pulling tower which feeds it through a furnace that heats the bottom of the platform  until it starts to melt the melted fiber preform then drops with the help of gravity down to a  capstan where a constant tension can be applied on the optical fiber as more melted fiber preform is
pulled it is monitored to ensure constant diameter within the acceptable range an acrylic coating is  then applied and cured for added protection and color for identification the fiber is  then coiled onto a fiber spool ready to be used to manufacture different types of fiber optic cables  let's have a look at the makeup of a standard optical fiber cord  we start off with a strand of optical fiber with a layer of cladding  the cladding is then over-sleeved with an acrylic coating  armamid yarn is then layered around the assembly to increase the tensile strength of the cord
the whole assembly is then protected with an outer cord jacket that is usually made with polyurethane  or pvc other than fiber cords some other fiber cable construction deployed around the world  are the slotted core cable drop cable ribbon cords and jumper cords the cable constructions  are constantly changing to increasing market demands and requirements for deployment well that's all the time we have we hope that you were able to learn something about  the various types of optical fibers and how they are made please like and subscribe to our
youtube channel for the latest updates and we will see you in our next video
"""


def main():
    IMAGE_DIR = "./images/rm_bg_chars/"
    char_to_image = get_char_to_image()
    output_image = text_to_handwritten_image(text, char_to_image, IMAGE_DIR)
    output_image.save("output.png")
    return


def get_char_to_image() -> dict:
    char_to_image = {}

    # 小文字
    for letter in string.ascii_lowercase:
        char_to_image[letter] = f"{letter}_lower.png"

    # 大文字
    for letter in string.ascii_uppercase:
        char_to_image[letter] = f"{letter}_upper.png"

    # 数字
    for number in string.digits:
        char_to_image[number] = f"{number}.png"

    # 記号
    char_to_image["'"] = "symbol_apostrophe.png"
    char_to_image[","] = "symbol_comma.png"
    char_to_image["!"] = "symbol_exclamation.png"
    char_to_image["."] = "symbol_period.png"
    char_to_image["?"] = "symbol_question.png"
    char_to_image[" "] = "symbol_space.png"

    return char_to_image


def text_to_handwritten_image(
    text, char_to_image, IMAGE_DIR, break_row_count=60
) -> Image:
    images = []
    row = []
    h, w = 0, 0
    for char in text:
        # 改行
        if char == " " or char not in char_to_image:
            if len(row) >= break_row_count:
                images.append(row)
                w = max(w, sum(img.width for img in row))
                row = []
        # イレギュラーの文字
        if char not in char_to_image:
            img_path = IMAGE_DIR + char_to_image[" "]
            img = Image.open(img_path)
            if img.mode == "RGBA":
                background = Image.new("RGB", img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[3])
                img = background
            row.append(img)
            continue

        img_path = IMAGE_DIR + char_to_image[char]
        img = Image.open(img_path)

        if img.mode == "RGBA":
            background = Image.new("RGB", img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[3])
            img = background
            h = max(h, img.height)
        row.append(img)
    else:
        images.append(row)
        w = max(w, sum(img.width for img in row))

    combined_image = Image.new("RGB", (w, h * len(images)), (255, 255, 255))
    y_offset = 0
    for images_row in images:
        x_offset = 0
        for img in images_row:
            combined_image.paste(img, (x_offset, y_offset))
            x_offset += img.width
        y_offset += h

    return combined_image


if __name__ == "__main__":
    main()
