let tg = window.Telegram.WebApp;
tg.expand();
tg.MainButton.textColor = "#FFFFFF";
tg.MainButton.color = "#BC8F8F";
let item = "";
let btn1 = document.getElementById("btn1");
let btn2 = document.getElementById("btn2");
let btn3 = document.getElementById("btn3");
let btn4 = document.getElementById("btn4");


btn1.addEventListener("click", function () {
    if (tg.MainButton.isVisible) {
        tg.MainButton.hide();
    }
    else {
        tg.MainButton.setText("Вывести информацию по Английскому языку");
        item = "1";
        tg.MainButton.show();
    }
});

btn2.addEventListener("click", function () {
    if (tg.MainButton.isVisible) {
        tg.MainButton.hide();
    }
    else {
        tg.MainButton.setText("Вывести информацию по Французскому языку");
        item = "2";
        tg.MainButton.show();
    }
});

btn3.addEventListener("click", function () {
    if (tg.MainButton.isVisible) {
        tg.MainButton.hide();
    }
    else {
        tg.MainButton.setText("Вывести информацию по Японскому языку");
        item = "3";
        tg.MainButton.show();
    }
});

btn4.addEventListener("click", function () {
    if (tg.MainButton.isVisible) {
        tg.MainButton.hide();
    }
    else {
        tg.MainButton.setText("Вывести информацию по Мотивационной цитате");
        item = "4";
        tg.MainButton.show();
    }
});

Telegram.WebApp.onEvent("mainButtonClicked", function () {
    tg.sendData(item);
});



web_app=WebAppInfo(url="https://anananastejsi.github.io/first/")

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Языки",web_app=web_app)]
    ],
    resize_keyboard=True
)


DISC = {
    '1': 'nice!!!',
    '2': 'good!!!',
    '3': 'awesome!!!',
    '4': 'hehehe'
}


@dp.message_handler(content_types='web_app_data')
async def buy_process(web_app_message):
    await bot.send_message(web_app_message.chat.id,
DISC[f'{web_app_message.web_app_data}'])
