#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Lang_Code:
    def __init__(self, origine, target):
        self.origine = self.__control_code(origine)
        self.target = self.__control_code(target)
        self.miss = 0 # number of lang can't be detected
        self.misslang = []
        self.langs = [("aa", "aar"),
                ("ab", "abk"),
                ("ae", "ave"),
                ("af", "afr"),
                ("ak", "aka"),
                ("am", "amh"),
                ("an", "arg"),
                ("ar", "ara"),
                ("as", "asm"),
                ("av", "ava"),
                ("ay", "aym"),
                ("az", "aze"),
                ("ba", "bak"),
                ("be", "bel"),
                ("bg", "bul"),
                ("bh", "und"),
                ("bi", "bis"),
                ("bm", "bam"),
                ("bn", "ben"),
                ("bo", "bod"),
                ("br", "bre"),
                ("bs", "bos"),
                ("ca", "cat"),
                ("ce", "che"),
                ("ch", "cha"),
                ("co", "cos"),
                ("cr", "cre"),
                ("cs", "ces"),
                ("cu", "chu"),
                ("cv", "chv"),
                ("cy", "cym"),
                ("da", "dan"),
                ("de", "deu"),
                ("dv", "div"),
                ("dz", "dzo"),
                ("ee", "ewe"),
                ("el", "ell"),
                ("en", "eng"),
                ("eo", "epo"),
                ("es", "spa"),
                ("et", "est"),
                ("eu", "eus"),
                ("fa", "fas"),
                ("ff", "ful"),
                ("fi", "fin"),
                ("fj", "fij"),
                ("fo", "fao"),
                ("fr", "fra"),
                ("fy", "fry"),
                ("ga", "gle"),
                ("gd", "gla"),
                ("gl", "glg"),
                ("gn", "grn"),
                ("gu", "guj"),
                ("gv", "glv"),
                ("ha", "hau"),
                ("he", "heb"),
                ("hi", "hin"),
                ("ho", "hmo"),
                ("hr", "hrv"),
                ("ht", "hat"),
                ("hu", "hun"),
                ("hy", "hye"),
                ("hz", "her"),
                ("ia", "ina"),
                ("id", "ind"),
                ("ie", "ile"),
                ("ig", "ibo"),
                ("ii", "iii"),
                ("ik", "ipk"),
                ("io", "ido"),
                ("is", "isl"),
                ("it", "ita"),
                ("iu", "iku"),
                ("ja", "jpn"),
                ("jv", "jav"),
                ("ka", "kat"),
                ("kg", "kon"),
                ("ki", "kik"),
                ("kj", "kua"),
                ("kk", "kaz"),
                ("kl", "kal"),
                ("km", "khm"),
                ("kn", "kan"),
                ("ko", "kor"),
                ("kr", "kau"),
                ("ks", "kas"),
                ("ku", "kur"),
                ("kv", "kom"),
                ("kw", "cor"),
                ("ky", "kir"),
                ("la", "lat"),
                ("lb", "ltz"),
                ("lg", "lug"),
                ("li", "lim"),
                ("ln", "lin"),
                ("lo", "lao"),
                ("lt", "lit"),
                ("lu", "lub"),
                ("lv", "lav"),
                ("mg", "mlg"),
                ("mh", "mah"),
                ("mi", "mri"),
                ("mk", "mkd"),
                ("ml", "mal"),
                ("mn", "mon"),
                ("mr", "mar"),
                ("ms", "msa"),
                ("mt", "mlt"),
                ("my", "mya"),
                ("na", "nau"),
                ("nb", "nob"),
                ("nd", "nde"),
                ("ne", "nep"),
                ("ng", "ndo"),
                ("nl", "nld"),
                ("nn", "nno"),
                ("no", "nor"),
                ("nr", "nbl"),
                ("nv", "nav"),
                ("ny", "nya"),
                ("oc", "oci"),
                ("oj", "oji"),
                ("om", "orm"),
                ("or", "ori"),
                ("os", "oss"),
                ("pa", "pan"),
                ("pi", "pli"),
                ("pl", "pol"),
                ("ps", "pus"),
                ("pt", "por"),
                ("qu", "que"),
                ("rm", "roh"),
                ("rn", "run"),
                ("ro", "ron"),
                ("ru", "rus"),
                ("rw", "kin"),
                ("sa", "san"),
                ("sc", "srd"),
                ("sd", "snd"),
                ("se", "sme"),
                ("sg", "sag"),
                ("sh", "hbs"),
                ("si", "sin"),
                ("sk", "slk"),
                ("sl", "slv"),
                ("sm", "smo"),
                ("sn", "sna"),
                ("so", "som"),
                ("sq", "sqi"),
                ("sr", "srp"),
                ("ss", "ssw"),
                ("st", "sot"),
                ("su", "sun"),
                ("sv", "swe"),
                ("sw", "swa"),
                ("ta", "tam"),
                ("te", "tel"),
                ("tg", "tgk"),
                ("th", "tha"),
                ("ti", "tir"),
                ("tk", "tuk"),
                ("tl", "tgl"),
                ("tn", "tsn"),
                ("to", "ton"),
                ("tr", "tur"),
                ("ts", "tso"),
                ("tt", "tat"),
                ("tw", "twi"),
                ("ty", "tah"),
                ("ug", "uig"),
                ("uk", "ukr"),
                ("ur", "urd"),
                ("uz", "uzb"),
                ("ve", "ven"),
                ("vi", "vie"),
                ("vo", "vol"),
                ("wa", "wln"),
                ("wo", "wol"),
                ("xh", "xho"),
                ("yi", "yid"),
                ("yo", "yor"),
                ("za", "zha"),
                ("zh", "zho"),
                ("zu", "zul"),
                ("und","und")]

        self.dict = {}
        self.__make_dict()

    def __control_code(self,coding):
        if coding == "ISO-639-1" or coding == "ISO639-1":
            coding = "ISO-639-1"
        elif coding == "ISO-639-3" or coding == "ISO639-3":
            coding = "ISO-639-3"
        else:
            raise "InputCodeError"
        return coding


    def __make_dict(self):
        if self.origine == "ISO-639-1":
            for x,y in self.langs:
                self.dict[x] = y
        elif self.origine == "ISO-639-3":
            for x,y in self.langs:
                self.dict[y] = x

    def set_targetCode(self, target):
        self.target = self.__control_code(target)
        self.dict = {}
        self.__make_dict()

    def set_origineCode(self, origine):
        self.origine = self.__control_code(origine)
        self.dict = {}
        self.__make_dict()

    def changeCode(self,string):
        try:
            return self.dict[string]
        except:
            self.miss += 1
            self.misslang.append(string)
            return "und"

    def get_noDetected(self):
        return self.miss, "_".join(self.misslang)

