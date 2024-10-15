
# حالات یک ماشین خودران بصورت کلی بصورت زیر است

#  در حالت اول توقف است
# حالت دوم در حال حرکت
# حالت سوم پارک است



# حالات بصورت دیکشنری

states = {
    "current": {
        "description": "ماشین متوقف است و در حالت فعلی است که منتظر دستور بعدی است",
        "actions": ["check_sensors", "plan_path"]
    },
    "driving": {
        "description": "ماشین در حال حرکت است",
        "actions": ["follow_path", "avoid_obstacles"]
    },
    "parking": {
        "description": "ماشین در حال پارک کردن است",
        "actions": ["find_parking_spot", "park"]
    }
}



def control_vehicle(self):
    # کنترل سرعت و جهت حرکت بر اساس تصمیمات گرفته شده
    if self.state == "driving":
        pass
        #follow-path
        # ... (الگوریتم‌های کنترل برای حفظ مسیر، تغییر سرعت و ...)
    elif self.state == "parking":
        pass
        # find_parking_spot
        # ... (الگوریتم‌های پارک کردن)
    elif self.state == "current":
        pass
        # check_sensors
        # ... (اقدامات اضطراری مانند ترمز کردن)


class SelfDrivingCar:
    def init(self):
        self.speed = 0  # سرعت فعلی ماشین (مثلاً بر حسب کیلومتر بر ساعت)
        self.direction = 0  # جهت حرکت ماشین (مثلاً زاویه نسبت به شمال)
        self.sensors = {
            "distance": [],  # فاصله تا موانع اطراف
            "camera": [],  # تصاویر گرفته شده توسط دوربین
            "radar": []  # داده‌های رادار (فاصله و سرعت اشیاء)
        }
        self.state = "idle"  # حالت فعلی ماشین (idle, driving, parking)
        self.path = []  # مسیر برنامه‌ریزی شده برای ماشین        