import random
import math
import time
import NeuralN
from copy import deepcopy


class Checkers:
    # Boolean True sets up the pieces on the game board. Boolean False does not.
    def __init__(self, boolean):
        self.gui_player = ""
        self.depth = 1
        self.whiteNNW = [-0.04465417649996872,-0.428626764106384,-0.5520841143869109,0.41523310942557967,0.11334573873449283,-0.38449285340594686,0.15806686001778936,-0.7049015123701475,0.8202870951126899,0.3643253929992586,0.524868843503747,-0.09073408206419553,-0.09465682320413782,0.2757377290143559,-0.665956364861846,0.4682334151384585,0.2942405607204216,-0.6810254488535612,-0.5771600585936977,0.5595502085931182,-0.6193736462306395,0.4115703367675482,0.39767762977253207,0.4998335657787927,-0.9923458734480486,-0.047031972930269506,-0.3135291024600787,-0.7258711464048602,-0.36500065717130714,0.15240285395709918,-0.03178676564145122,0.2636660469352081,-0.07551108106061133,0.3687052043203227,-0.2374398763503669,0.21513325573453335,-0.3464825909125191,0.6555603405656327,0.8448830408132472,-0.8573502737242239,0.13274501091350133,-0.3846930512007207,-0.7492390844529719,0.9275423189000767,0.14709388306437654,0.9430934005806948,0.2050925307012268,-0.5899182188219745,0.8751389484268831,-0.35492768830072907,0.5037197316964139,0.41217590063347254,-0.8760022901732388,-0.8070892310207924,0.22317886168650114,0.94369913704104,0.5974647530100493,-0.5815006926070247,-0.33177490055295544,-0.5357711543246872,-0.3404091769135036,-0.3546986955766851,0.9818831190533924,-0.6707469650107309,-0.7905904964715649,-0.12796130766685698,-0.671073024818051,-0.36265484189252184,0.5768854037587117,-0.8165980007215736,0.63899533840601,-0.4799669789777694,0.8334526615574563,-0.41689796443488936,-0.2619312523133561,-0.9551882402906063,-0.7153046438379823,0.3763475805150214,-0.7815088278274079,-0.5372617183135886,-0.08874996966390791,0.6851579072275084,0.03649125118134944,-0.8705487347977603,-0.6354853915245862,-0.5040218317359486,0.052442973514778,-0.9007183816165368,-0.9793713515120562,-0.9685457003755796,0.8252140348070519,0.7518046822218665,-0.9200423933128032,0.7227671299285993,-0.6212361261095323,0.4794398928911471,-0.09421244664429995,0.8337728921918328,-0.7485680193586094,-0.9980501491911627,-0.7902879932981326,-0.87454791169441,0.8910237246557738,-0.20411337204039148,-0.021325932161111005,0.8680892505252863,0.4107370235925233,0.22302638948349218,0.12918067031320402,0.7047765168777718,0.008142528396893445,0.39084422847688716,0.9832031852975589,0.9449772646734722,-0.04852269107969753,-0.31038720336707537,-0.5507529175075393,0.5465880616675073,-0.7104714270497428,-0.5972548118631303,0.7108617492271102,-0.01434260084283312,0.042692340918614846,0.6117884089367497,0.6894034886295453,0.25076479897343706,0.004172662752264911,-0.9781662590379854,-0.31174172340064443,0.046805793259470097,0.8363626023123053,-0.2109374779006098,0.5470794467070115,0.1890778805663461,0.25204713029216275,0.7221950113852876,-0.3232370367917603,-0.2027715772590427,0.13700866202523465,0.2855291218240156,0.8100282086398582,0.08615763530996945,0.6593500419666922,-0.5461623562305649,-0.12365627692098557,0.09616391085201292,0.7566127977501608,-0.8225081451351475,0.014219832015500367,-0.11808640790882752,0.012273036464592657,-0.07161952372867819,0.039788058952329175,0.5849577088045069,-0.6156087256190585,-0.432421893280981,0.021374339060108105,-0.6572368079788522,-0.09115960860114647,-0.7505720170058156,0.078200789621236,-0.8697016871267672,-0.9051522030671092,0.48365643104243405,0.4207785147038644,-0.5266638728028142,-0.08624575533448853,0.2579808808702795,0.09095343499059283,0.47578464381834895,0.8437683819439359]
        self.blackNNW = [-0.04465417649996872,-0.428626764106384,-0.5520841143869109,0.41523310942557967,0.11334573873449283,-0.38449285340594686,0.15806686001778936,-0.7049015123701475,0.8202870951126899,0.3643253929992586,0.524868843503747,-0.09073408206419553,-0.09465682320413782,0.2757377290143559,-0.665956364861846,0.4682334151384585,0.2942405607204216,-0.6810254488535612,-0.5771600585936977,0.5595502085931182,-0.6193736462306395,0.4115703367675482,0.39767762977253207,0.4998335657787927,-0.9923458734480486,-0.047031972930269506,-0.3135291024600787,-0.7258711464048602,-0.36500065717130714,0.15240285395709918,-0.03178676564145122,0.2636660469352081,-0.07551108106061133,0.3687052043203227,-0.2374398763503669,0.21513325573453335,-0.3464825909125191,0.6555603405656327,0.8448830408132472,-0.8573502737242239,0.13274501091350133,-0.3846930512007207,-0.7492390844529719,0.9275423189000767,0.14709388306437654,0.9430934005806948,0.2050925307012268,-0.5899182188219745,0.8751389484268831,-0.35492768830072907,0.5037197316964139,0.41217590063347254,-0.8760022901732388,-0.8070892310207924,0.22317886168650114,0.94369913704104,0.5974647530100493,-0.5815006926070247,-0.33177490055295544,-0.5357711543246872,-0.3404091769135036,-0.3546986955766851,0.9818831190533924,-0.6707469650107309,-0.7905904964715649,-0.12796130766685698,-0.671073024818051,-0.36265484189252184,0.5768854037587117,-0.8165980007215736,0.63899533840601,-0.4799669789777694,0.8334526615574563,-0.41689796443488936,-0.2619312523133561,-0.9551882402906063,-0.7153046438379823,0.3763475805150214,-0.7815088278274079,-0.5372617183135886,-0.08874996966390791,0.6851579072275084,0.03649125118134944,-0.8705487347977603,-0.6354853915245862,-0.5040218317359486,0.052442973514778,-0.9007183816165368,-0.9793713515120562,-0.9685457003755796,0.8252140348070519,0.7518046822218665,-0.9200423933128032,0.7227671299285993,-0.6212361261095323,0.4794398928911471,-0.09421244664429995,0.8337728921918328,-0.7485680193586094,-0.9980501491911627,-0.7902879932981326,-0.87454791169441,0.8910237246557738,-0.20411337204039148,-0.021325932161111005,0.8680892505252863,0.4107370235925233,0.22302638948349218,0.12918067031320402,0.7047765168777718,0.008142528396893445,0.39084422847688716,0.9832031852975589,0.9449772646734722,-0.04852269107969753,-0.31038720336707537,-0.5507529175075393,0.5465880616675073,-0.7104714270497428,-0.5972548118631303,0.7108617492271102,-0.01434260084283312,0.042692340918614846,0.6117884089367497,0.6894034886295453,0.25076479897343706,0.004172662752264911,-0.9781662590379854,-0.31174172340064443,0.046805793259470097,0.8363626023123053,-0.2109374779006098,0.5470794467070115,0.1890778805663461,0.25204713029216275,0.7221950113852876,-0.3232370367917603,-0.2027715772590427,0.13700866202523465,0.2855291218240156,0.8100282086398582,0.08615763530996945,0.6593500419666922,-0.5461623562305649,-0.12365627692098557,0.09616391085201292,0.7566127977501608,-0.8225081451351475,0.014219832015500367,-0.11808640790882752,0.012273036464592657,-0.07161952372867819,0.039788058952329175,0.5849577088045069,-0.6156087256190585,-0.432421893280981,0.021374339060108105,-0.6572368079788522,-0.09115960860114647,-0.7505720170058156,0.078200789621236,-0.8697016871267672,-0.9051522030671092,0.48365643104243405,0.4207785147038644,-0.5266638728028142,-0.08624575533448853,0.2579808808702795,0.09095343499059283,0.47578464381834895,0.8437683819439359]
        self.whiteNN = NeuralN.NeuralNetwork()
        self.blackNN = NeuralN.NeuralNetwork()
        self.whiteNN.updateWeights(self.whiteNNW)
        self.blackNN.updateWeights(self.blackNNW)

        self.board_vector = [0 for i in range(32)]

        if boolean:
            self.__setBoard()

    # Sets the pieces on the board to all initial positions.
    def __setBoard(self):
        for i in range(12):
            self.board_vector[i] = 1
        for i in range(12, 20):
            self.board_vector[i] = 0
        for i in range(20, 32):
            self.board_vector[i] = -1

    def setBoard(self):
        self.__setBoard()

    def showBoardIndices(self):
        print("Board Indices")
        output = [[i for i in range(4)] for j in range(8)]
        k = 31
        for i in range(len(output)):
            for j in range(len(output[i])):
                output[i][j] = k
                k -= 1
        for i in range(8):
            output[i] = output[i][::-1]

        k = 0
        print("  " + chr(9135) * 18)
        for i in output:
            print("  " + chr(9122), end='')
            if k % 2 == 0:
                print("  ", end='')
            for j in i:
                if j == 31 or j == 23 or j == 15 or j == 7:
                    print(str(j), end='')
                else:
                    print(str(j) + "  ", end='')
                if j < 10:
                    print(" ", end='')
            print(chr(9130))
            k += 1
        print("  " + chr(9146) * 18)

    # prints board to standard output
    def showBoard(self, brdcpy):
        output = [0 for i in range(64)]
        for i in range(32):
            if (0 <= (i % 8) < 4):
                output[i * 2] = brdcpy[i]
            else:
                output[(i * 2) + 1] = brdcpy[i]

        board = [0 for i in range(8)]
        for i in range(8):
            board[i] = [0 for i in range(8)]
        for i in range(64):
            if (output[i] == 1):
                board[i // 8][i % 8] = "w"
            elif (output[i] == -1):
                board[i // 8][i % 8] = "b"
            elif (output[i] == 2):
                board[i // 8][i % 8] = "W"
            elif (output[i] == -2):
                board[i // 8][i % 8] = "B"
            else:
                board[i // 8][i % 8] = "0"
        for i in range(7, -1, -1):
            print(board[i])

    # prints board to standard output.  Better formatting than showBoard()
    def showBoardV2(self):
        output = [0 for i in range(64)]
        for i in range(32):
            if (0 <= (i % 8) < 4):
                output[i * 2] = self.board_vector[i]
            else:
                output[(i * 2) + 1] = self.board_vector[i]

        board = [0 for i in range(8)]
        for i in range(8):
            board[i] = [0 for i in range(8)]
        for i in range(64):
            if (output[i] == 1):
                board[i // 8][i % 8] = "w"
            elif (output[i] == -1):
                board[i // 8][i % 8] = "b"
            elif (output[i] == 2):
                board[i // 8][i % 8] = "W"
            elif (output[i] == -2):
                board[i // 8][i % 8] = "B"
            else:
                board[i // 8][i % 8] = "_"

        board2 = [0 for i in range(8)]
        for i in range(7, -1, -1):
            board2[int(math.fabs(i - 7))] = board[i]

        print("-" * 41)
        for i in range(8):
            print("|     ", end='')
            for j in board2[i]:
                print(j, "  ", end='')
            print("  |")
            print("|     ", end='')
            if (i % 2 == 0):
                print("    ", end='')
            for k in range(int((math.fabs(i - 8) * 4) - 4), int(math.fabs(i - 8) * 4), 1):
                print(k, "   ", end='')
                if (k % 8 == 7):
                    if (k == 7):
                        print(" ", end='')
                elif (k % 8 == 3):
                    if (k == 3):
                        print("     ", end='')
                    else:
                        print("    ", end='')
                elif (k < 10):
                    print("   ", end='')
                else:
                    print("  ", end='')
            print("|")
        print("-" * 41)

    # prints board to standard output.  Better formatting than showBoard()
    def showBoardV2_5(self):
        output = [99 for i in range(64)]
        for i in range(32):
            if (0 <= (i % 8) < 4):
                output[i * 2] = self.board_vector[i]
            else:
                output[(i * 2) + 1] = self.board_vector[i]

        board = [0 for i in range(8)]
        for i in range(8):
            board[i] = [0 for i in range(8)]
        for i in range(64):
            if (output[i] == 1):
                board[i // 8][i % 8] = chr(9863)
            elif (output[i] == -1):
                board[i // 8][i % 8] = chr(9865)
            elif (output[i] == 2):
                board[i // 8][i % 8] = chr(9450)
            elif (output[i] == -2):
                board[i // 8][i % 8] = chr(9471)
            elif (output[i] == 0):
                board[i // 8][i % 8] = chr(9633)
            else:
                board[i // 8][i % 8] = chr(9632)

        board2 = [0 for i in range(8)]
        for i in range(7, -1, -1):
            board2[int(math.fabs(i - 7))] = board[i]

        print("-" * 41)
        for i in range(8):
            print("|     ", end='')
            for j in board2[i]:
                print(j, "  ", end='')
            print("  |")
            print("|     ", end='')
            if (i % 2 == 0):
                print("    ", end='')
            for k in range(int((math.fabs(i - 8) * 4) - 4), int(math.fabs(i - 8) * 4), 1):
                print(k, "   ", end='')
                if (k % 8 == 7):
                    if (k == 7):
                        print(" ", end='')
                elif (k % 8 == 3):
                    if (k == 3):
                        print("     ", end='')
                    else:
                        print("    ", end='')
                elif (k < 10):
                    print("   ", end='')
                else:
                    print("  ", end='')
            print("|")
        print("-" * 41)

    # prints board to standard output.  Better formatting than showBoard()
    def showBoardV3(self):
        output = [99 for i in range(64)]
        for i in range(32):
            if (0 <= (i % 8) < 4):
                output[i * 2] = self.board_vector[i]
            else:
                output[(i * 2) + 1] = self.board_vector[i]

        board = [0 for i in range(8)]
        for i in range(8):
            board[i] = [0 for i in range(8)]
        for i in range(64):
            if (output[i] == 1):
                board[i // 8][i % 8] = chr(9863)
            elif (output[i] == -1):
                board[i // 8][i % 8] = chr(9865)
            elif (output[i] == 2):
                board[i // 8][i % 8] = chr(9450)
            elif (output[i] == -2):
                board[i // 8][i % 8] = chr(9471)
            elif (output[i] == 0):
                board[i // 8][i % 8] = chr(9633)
            else:
                board[i // 8][i % 8] = chr(9632)

        board2 = [0 for i in range(8)]
        for i in range(7, -1, -1):
            board2[int(math.fabs(i - 7))] = board[i]

        print("  " + chr(9135) * 18)
        for i in range(8):
            # print(str((i-7)*-1) + " ", end="")
            print("  ", end='')
            print(chr(9122), end='')
            for j in board2[i]:
                print(j + " ", end='')
            print(chr(9130))
        print("  " + chr(9146) * 18)

    # variable "type" is an integer denoting the type of piece. 1 for normal piece 2 for King.
    # variable "p" is an array of the current board positions
    def findSingleMoves(self, p, player_type):
        moves = []
        for i in range(32):
            lm = -1;
            rm = -1
            if 28 <= i < 32:
                lm = -1;
                rm = -1
            elif 0 <= (i % 8) < 4:
                if (p[i + 4] == 0 and p[i] == player_type):
                    rm = i + 4
                if (i % 8) == 0:
                    lm = -1
                else:
                    if (p[i + 3] == 0 and p[i] == player_type):
                        lm = i + 3
            elif 4 <= (i % 8) < 8:
                if (p[i + 4] == 0 and p[i] == player_type):
                    lm = i + 4
                if (i % 8) == 7:
                    rm = -1
                else:
                    if (p[i + 5] == 0 and p[i] == player_type):
                        rm = i + 5
            moves.append([i, [lm, rm]])
        return moves

    # variable "type" is an integer denoting the type of piece. -1 for normal piece -2 for King.
    # variable "p" is an array of the current board positions
    def findSingleMovesReverse(self, p, player_type):
        moves = []
        for i in range(32):
            lm = -1;
            rm = -1
            if 0 <= i < 4:
                lm = -1;
                rm = -1
            elif 0 <= (i % 8) < 4:
                if (p[i - 4] == 0 and p[i] == player_type):
                    lm = i - 4
                if (i % 8) == 0:
                    rm = -1
                else:
                    if (p[i - 5] == 0 and p[i] == player_type):
                        rm = i - 5
            elif 4 <= (i % 8) < 8:
                if (p[i - 4] == 0 and p[i] == player_type):
                    rm = i - 4
                if (i % 8) == 7:
                    lm = -1
                else:
                    if (p[i - 3] == 0 and p[i] == player_type):
                        lm = i - 3
            moves.append([i, [lm, rm]])
        return moves

    # Calculates all possible forward jump moves for a single piece.
    # Returns moves as a list of the form; [lm, rm]
    def findJumpsSinglePiece(self, p, indx, player_type):
        lm = -1
        rm = -1
        i = indx
        if 24 <= i < 32:
            lm = -1;
            rm = -1
        elif 0 <= (i % 8) < 4:
            if (i % 8) == 3:
                rm = -1
            else:
                if (p[i] == player_type and (p[i + 4] * p[i]) < 0 and p[i + 9] == 0):
                    rm = i + 9
                else:
                    rm = -1
            if (i % 8) == 0:
                lm = -1
            else:
                if (p[i] == player_type and (p[i + 3] * p[i]) < 0 and p[i + 7] == 0):
                    lm = i + 7
                else:
                    lm = -1
        elif 4 <= (i % 8) < 8:
            if (i % 8) == 7:
                rm = -1
            else:
                if (p[i] == player_type and (p[i + 5] * p[i]) < 0 and p[i + 9] == 0):
                    rm = i + 9
                else:
                    rm = -1
            if (i % 8) == 4:
                lm = -1
            else:
                if (p[i] == player_type and (p[i + 4] * p[i]) < 0 and p[i + 7] == 0):
                    lm = i + 7
                else:
                    lm = -1
        return [lm, rm]

    # Returns a list of all possible forward jump moves of the form; [[0, [lm, rm]], [1, [lm, rm]]]
    def findJumps(self, p, player_type):
        moves = []
        for i in range(32):
            m_arr = self.findJumpsSinglePiece(p, i, player_type)
            moves.append([i, m_arr])
        return moves

    # Calculates all possible reverse jump moves for a single piece.
    # Returns moves as a list of the form; [lm, rm]
    def findJumpsReverseSinglePiece(self, p, indx, player_type):
        lm = -1
        rm = -1
        i = indx
        if 0 <= i < 8:
            lm = -1;
            rm = -1
        elif 0 <= (i % 8) < 4:
            if (i % 8) == 3:
                lm = -1
            else:
                if (p[i] == player_type and (p[i - 4] * p[i]) < 0 and p[i - 7] == 0):
                    lm = i - 7
                else:
                    lm = -1
            if (i % 8) == 0:
                rm = -1
            else:
                if (p[i] == player_type and (p[i - 5] * p[i]) < 0 and p[i - 9] == 0):
                    rm = i - 9
                else:
                    rm = -1
        elif 4 <= (i % 8) < 8:
            if (i % 8) == 7:
                lm = -1
            else:
                if (p[i] == player_type and (p[i - 3] * p[i]) < 0 and p[i - 7] == 0):
                    lm = i - 7
                else:
                    lm = -1
            if (i % 8) == 4:
                rm = -1
            else:
                if (p[i] == player_type and (p[i - 4] * p[i]) < 0 and p[i - 9] == 0):
                    rm = i - 9
                else:
                    rm = -1
        return [lm, rm]

    # Returns a list of all posible reverse jump moves of the form; [[0, [lm, rm]], [1, [lm, rm]]]
    # Takes in variables p, which is the board vector, indx, which is the index of the piece to be moved,
    # and type which is the player type.
    def findJumpsReverse(self, p, player_type):
        moves = []
        for i in range(32):
            m_arr = self.findJumpsReverseSinglePiece(p, i, player_type)
            moves.append([i, m_arr])
        return moves

    # variable "type" is an integer denoting the type of piece. 2 White -2 Black
    # variable "p" is an array of the current board positions
    def findKingMoves(self, p, player_type):
        arr1 = self.findSingleMoves(p, player_type)
        arr2 = self.findSingleMovesReverse(p, player_type)
        moves = []
        for i in range(32):
            temp = []
            temp.extend(arr1[i][1])
            temp.extend(arr2[i][1])
            moves.append([i, temp])
        return moves

    # Returns an array of all moves that all King pieces can jump to.
    # Takes in variables p, which is the board vector, and type which is the player type.
    def findKingJumps(self, p, type):
        arr1 = self.findJumps(p, type)
        arr2 = self.findJumpsReverse(p, type)
        moves = []
        for i in range(32):
            temp = []
            temp.extend(arr1[i][1])
            temp.extend(arr2[i][1])
            moves.append([i, temp])
        return moves

    # Returns an array of the positions that a single King piece can jump to.
    # Takes in variables p, which is the board vector, indx, which is the index of the piece to be moved,
    # and type which is the player type.
    def findKingJumpsSinglePiece(self, p, indx, type):
        arr = self.findJumpsSinglePiece(p, indx, type) + self.findJumpsReverseSinglePiece(p, indx, type)
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == -1:
                arr.pop(i)
        return arr

    # Removes the -1 values from the array of moves provided and then returns it.
    def removeNoMove(self, arr):
        moves = []
        for i in arr:
            temp = []
            for j in i[1]:
                if j >= 0:
                    temp.append(j)
            if temp != []:
                moves.append([i[0], temp])
        return moves

    # Returns a random move for the random player.
    # Takes in arr of possible jumps.
    def selectRandomMove(self, arr):
        rng1 = random.randrange(0, len(arr))
        rng2 = random.randrange(0, len(arr[rng1][1]))
        return [arr[rng1][0], arr[rng1][1][rng2]]

    # Returns a random jump move for the inner jumps of the random player.
    # Takes in arr of possible jumps.
    def selectRandomInnerJump(self, arr):
        rng1 = random.randrange(0, len(arr[1]))
        return [arr[0], arr[1][rng1]]

    # Removes inner brackets from array move.
    def cleanSelectedMove(self, arr):
        return [arr[0], arr[1][0]]

    # Takes in array of moves with format [[1, [2]], [3, [4, 5]]] and returns an array with format [[1, 2], [3, 4], [3, 5]].
    def cleanArrayMoves(self, arr):
        output_arr = []
        for move in arr:
            if isinstance(move[1], list):
               for sub_move in move[1]:
                output_arr.append([move[0], sub_move])
            else:
                output_arr.append(move)
        return output_arr

    # sm = [x1, x2], x1, x2 are integers. x1 the original position of the piece. x2 the position for the piece to be moved to.
    # Variable p is vector representing the checkers board.
    def movePieceNN(self, p, sm):
        temp = self.__checkForKingNN(p, sm)
        test = sm[0] - sm[1]
        if (test > 0):
            if (test == 7):
                if (0 <= sm[0] % 8 < 4):
                    p[sm[0] - 4] = 0
                elif (4 <= sm[0] % 8 < 8):
                    p[sm[0] - 3] = 0
            elif (test == 9):
                if (0 <= sm[0] % 8 < 4):
                    p[sm[0] - 5] = 0
                elif (4 <= sm[0] % 8 < 8):
                    p[sm[0] - 4] = 0
        else:
            if (test == -7):
                if (0 <= sm[0] % 8 < 4):
                    p[sm[0] + 3] = 0
                elif (4 <= sm[0] % 8 < 8):
                    p[sm[0] + 4] = 0
            elif (test == -9):
                if (0 <= sm[0] % 8 < 4):
                    p[sm[0] + 4] = 0
                elif (4 <= sm[0] % 8 < 8):
                    p[sm[0] + 5] = 0
        p[sm[0]] = 0
        p[sm[1]] = temp
    #    self.showBoardV3()

    # sm = [x1, x2], x1, x2 are integers. x1 the original position of the piece. x2 the position for the piece to be moved to.
    def movePiece(self, sm):
        temp = self.__checkForKing(sm)
        test = sm[0] - sm[1]
        if (test > 0):
            if (test == 7):
                if (0 <= sm[0] % 8 < 4):
                    self.board_vector[sm[0] - 4] = 0
                elif (4 <= sm[0] % 8 < 8):
                    self.board_vector[sm[0] - 3] = 0
            elif (test == 9):
                if (0 <= sm[0] % 8 < 4):
                    self.board_vector[sm[0] - 5] = 0
                elif (4 <= sm[0] % 8 < 8):
                    self.board_vector[sm[0] - 4] = 0
        else:
            if (test == -7):
                if (0 <= sm[0] % 8 < 4):
                    self.board_vector[sm[0] + 3] = 0
                elif (4 <= sm[0] % 8 < 8):
                    self.board_vector[sm[0] + 4] = 0
            elif (test == -9):
                if (0 <= sm[0] % 8 < 4):
                    self.board_vector[sm[0] + 4] = 0
                elif (4 <= sm[0] % 8 < 8):
                    self.board_vector[sm[0] + 5] = 0
        self.board_vector[sm[0]] = 0
        self.board_vector[sm[1]] = temp

    # Removes -1 from list.  Takes in [9, -1] and returns [9] or takes in [1, 2] and returns [1, 2].
    # Used in conjunction with findJumpsSinglePiece() function.
    def removeNegatives(self, arr):
        temp = []
        for i in range(len(arr)):
            if arr[i] != -1:
                temp.append(arr[i])
        return temp

    # Calculates all jump possibilities from given jump for a single piece.  Returns list of branching jumps.
    def calculateJumpPaths(self, jump, boardCopy):
        self.movePieceNN(boardCopy, jump)
        type = boardCopy[jump[1]]
        # print("move made -", jump)
        # print("type -", boardCopy[jump[1]])
        if type == 1:
            njs = self.removeNegatives(self.findJumpsSinglePiece(boardCopy, jump[1], type))
        elif type == -1:
            njs = self.removeNegatives(self.findJumpsReverseSinglePiece(boardCopy, jump[1], type))
        else:
            njs = self.findKingJumpsSinglePiece(boardCopy, jump[1], type)
        # print("njs -", njs)

        temp = []
        if len(njs) == 0:
            temp.append(jump)
        elif len(njs) == 1:
            # print("len 1", njs, "jump", jump)
            nextJump = [jump[1], njs[0]]
            temp.append(jump)
            temp.append(self.calculateJumpPaths(nextJump, boardCopy))
        elif len(njs) == 2:
            # print("len 2", njs, "jump", jump)
            nextJump = [jump[1], njs[0]]
            nextJump2 = [jump[1], njs[1]]
            temp.append(jump)
            temp.append(self.calculateJumpPaths(nextJump, boardCopy[:]))
            temp.append(self.calculateJumpPaths(nextJump2, boardCopy[:]))
        else:
            # print("len 3", njs)
            nextJump = [jump[1], njs[0]]
            nextJump2 = [jump[1], njs[1]]
            nextJump3 = [jump[1], njs[2]]
            temp.append(jump)
            temp.append(self.calculateJumpPaths(nextJump, boardCopy[:]))
            temp.append(self.calculateJumpPaths(nextJump2, boardCopy[:]))
            temp.append(self.calculateJumpPaths(nextJump3, boardCopy[:]))
        return temp

    # Returns an array of all possible jump paths from given array input.
    # Input is an array of jumps that can be made following the first.
    # Input comes from calculateJumpPaths() function output.
    def createJumpPathsBuilder(self, arr):
        narr = self.flattenJumpPathArray(arr)
        output = []
        narr_copy = narr[:]

        pathEnds = []
        for i in range(1, len(narr_copy) - 1):
            if narr_copy[i][1] != narr_copy[i + 1][0] or (
                    narr_copy[i][1] == narr_copy[i + 1][0] and narr_copy[i][0] == narr_copy[i + 1][1]):
                pathEnds.append(i)
        pathEnds.append(len(narr_copy) - 1)
        pathE = pathEnds[::-1]

        for i in range(len(pathE)):
            output.append([])

        for i in range(len(output)):
            # print("\npath")
            temp = narr_copy[pathE[i]][:]
            output[i].append(temp)
            for j in range(pathE[i] - 1, -1, -1):
                # print("temp", temp, "next", narr_copy[i])
                if temp[0] == narr_copy[j][1] and temp[1] == narr_copy[j][0]:
                    continue
                elif temp[0] == narr_copy[j][1]:
                    # print("appended", narr_copy[i], "to", path)
                    output[i].append(narr_copy[j][:])
                    temp = narr_copy[j][:]

        for i in range(len(output)):
            output[i] = output[i][::-1]
        return output

    # Takes an array of arrays as input and returns a flattened array. Works within createJumpPathsBuilder() function.
    # Ex: [[3, 10], [[10, 17]], [[10, 19]]] -> [[3, 10], [10, 17], [10, 19]]
    def flattenJumpPathArray(self, arr):
        output = []
        if isinstance(arr[0], int):
            return [arr]
        for jump in arr:
            if isinstance(jump[0], int):
                output.append(jump)
            else:
                for nJump in jump:
                    output.extend(self.flattenJumpPathArray(nJump))
        return output

    # Determine if a piece needs to be Kinged
    # sm = [x1, x2], x1, x2 are integers. x1 the original position of the piece. x2 the position for the piece to be moved to.
    def __checkForKing(self, sm):
        if (self.board_vector[sm[0]] == 1):
            if (28 <= sm[1] < 32):
                return 2
            else:
                return 1
        elif (self.board_vector[sm[0]] == -1):
            if (0 <= sm[1] < 4):
                return -2
            else:
                return -1
        else:
            return self.board_vector[sm[0]]

    # Determine if a piece needs to be Kinged.  Works in movePieceNN in CalculateJumpsPaths due to boardCopies.
    # sm = [x1, x2], x1, x2 are integers. x1 the original position of the piece. x2 the position for the piece to be moved to.
    def __checkForKingNN(self, p, sm):
        if (p[sm[0]] == 1):
            if (28 <= sm[1] < 32):
                return 2
            else:
                return 1
        elif (p[sm[0]] == -1):
            if (0 <= sm[1] < 4):
                return -2
            else:
                return -1
        else:
            return p[sm[0]]

    # returns array [w, b] containing w: number of white pieces, b: number of black pieces on the board.
    def __countPieces(self):
        b = 0
        w = 0
        for i in self.board_vector:
            if (i == 1 or i == 2):
                w += 1
            elif (i == -1 or i == -2):
                b += 1
        return [w, b]

    # Returns the index of the maximum value within a given array a.  Array must contain number values.
    @staticmethod
    def indxOfMax(a):
        if (len(a) == 0):
            print("array empty")
        else:
            indx = 0
            max = 0
            for i in range(len(a)):
                if (a[i] > max):
                    max = a[i]
                    indx = i
            return indx

    # Checks the game board to determine if a player has won.  Based on amount of pieces remaining.
    # Returns 'w' when the white player wins and 'b' when the black player wins.
    def __checkVictory(self):
        wb = self.__countPieces()
        if wb[0] == 0:
            # print("Black Victory.  All Pieces Taken.")
            return 'b'
        elif wb[1] == 0:
            # print("White Victory.  All Pieces Taken.")
            return 'w'

    def checkVictory(self):
        wb = self.__countPieces()
        if wb[0] == 0:
            # print("Black Victory.  All Pieces Taken.")
            return 'b'
        elif wb[1] == 0:
            # print("White Victory.  All Pieces Taken.")
            return 'w'

    def checkend(self):
        wb = self.__countPieces()
        if wb[0] == 0 or wb[1] ==0:
            return True
        else:
            return False

    # Variable boolean either True or False to show game board.
    def game(self, boolean):
        if boolean:
            self.showBoard()
            print("\n")
        c = 0
        while (c < 100):
            c += 1
            if (c % 2 == 1):
                moves = self.removeNoMove(self.findSingleMoves(self.board_vector, 1))
                jumpmoves = self.removeNoMove(self.findJumps(self.board_vector, 1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, 2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, 2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps
                if boolean:  # info on possible moves
                    print("\nall moves -", am)
                    print("all jumps -", jm, "\n")
                if (jm == [] and am == []):
                    # print("Black Victory. White can't move.")
                    return 'b'
                elif (jm == []):
                    selMove = self.selectRandomMove(am)
                    self.movePiece(selMove)
                    if (boolean):
                        print("selected move", selMove)
                else:
                    selMove = self.selectRandomMove(jm)
                    self.movePiece(selMove)
                    if boolean:  # info on possible moves
                        print("selected move", selMove)
                    jm = self.removeNoMove(self.findJumps(self.board_vector, 1)) + self.removeNoMove(
                        self.findKingJumps(self.board_vector, 2))
                    while (jm != []):
                        tp1 = jm
                        if boolean:  # info on possible moves
                            print("new jumps -", jm)
                        for i in jm:
                            if (i[0] == selMove[1]):
                                selMove = self.selectRandomInnerJump(i)
                                self.movePiece(selMove)
                                if boolean:  # info on possible moves
                                    print("selected move", selMove)
                        if (jm == tp1):
                            break
                        jm = self.removeNoMove(self.findJumps(self.board_vector, 1)) + self.removeNoMove(
                            self.findKingJumps(self.board_vector, 2))
            else:
                moves = self.removeNoMove(self.findSingleMovesReverse(self.board_vector, -1))
                jumpmoves = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, -2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, -2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps
                if boolean:  # info on possible moves
                    print("\nall moves -", am)
                    print("all jumps -", jm, "\n")
                if (jm == [] and am == []):
                    # print("White Victory. Black can't move.")
                    return 'w'
                elif (jm == []):
                    selMove = self.selectRandomMove(am)
                    self.movePiece(selMove)
                    if (boolean):
                        print("selected move", selMove)
                else:
                    selMove = self.selectRandomMove(jm)
                    self.movePiece(selMove)
                    if boolean:  # info on possible moves
                        print("selected move", selMove)
                    jm = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1)) + self.removeNoMove(
                        self.findKingJumps(self.board_vector, -2))
                    while (jm != []):
                        tp1 = jm
                        if boolean:  # info on possible moves
                            print("new jumps -", jm)
                        for i in jm:
                            if (i[0] == selMove[1]):
                                selMove = self.selectRandomInnerJump(i)
                                self.movePiece(selMove)
                                if boolean:  # info on possible moves
                                    print("selected move", selMove)
                        if (jm == tp1):
                            break
                        jm = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1)) + self.removeNoMove(
                            self.findKingJumps(self.board_vector, -2))
            if (boolean):
                print("iteration:", c)
                self.showBoard()
            tester = self.__checkVictory()
            if tester == 'w':
                return 'w'
            elif tester == 'b':
                return 'b'
        return "d"


    # Variable boolean either True or False to show game board.
    def gameTest(self, boolean):
        print("Game Start")
        # board_vector[14] = 1; board_vector[18] = -1; board_vector[19] = -1; board_vector[25] = -1; board_vector[20] = 1
        self.showBoardV2()
        print("\n")
        c = 0
        while (c < 100):
            c += 1
            if (c % 2 == 1):
                moves = self.removeNoMove(self.findSingleMoves(self.board_vector, 1))
                jumpmoves = self.removeNoMove(self.findJumps(self.board_vector, 1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, 2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, 2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps
                print("\nall moves -", am)
                print("all jumps -", jm, "\n")
                if (jm == [] and am == []):
                    # print("Black Victory. White can't move.")
                    return 'b'
                elif (jm == []):
                    selMove = self.selectRandomMove(am)
                    self.movePiece(selMove)
                    print("selected move -", selMove)
                else:
                    selMove = self.selectRandomMove(jm)
                    self.movePiece(selMove)
                    print("selected move", selMove)
                    jm = self.removeNoMove(self.findJumps(self.board_vector, 1)) + self.removeNoMove(
                        self.findKingJumps(self.board_vector, 2))
                    while (jm != []):
                        tp1 = jm
                        if boolean:  # info on possible moves
                            print("new jumps -", jm)
                        for i in jm:
                            if (i[0] == selMove[1]):
                                selMove = self.selectRandomInnerJump(i)
                                self.movePiece(selMove)
                                print("selected move", selMove)
                        if (jm == tp1):
                            break
                        jm = self.removeNoMove(self.findJumps(self.board_vector, 1)) + self.removeNoMove(
                            self.findKingJumps(self.board_vector, 2))
            else:
                moves = self.removeNoMove(self.findSingleMovesReverse(self.board_vector, -1))
                jumpmoves = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, -2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, -2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps
                print("\nall moves -", am)
                print("all jumps -", jm, "\n")
                if (jm == [] and am == []):
                    # print("White Victory. Black can't move.")
                    return 'w'
                elif (jm == []):
                    selMove = self.selectRandomMove(am)
                    self.movePiece(selMove)
                    print("selected move -", selMove)
                else:
                    selMove = self.selectRandomMove(jm)
                    self.movePiece(selMove)
                    print("selected move", selMove)
                    jm = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1)) + self.removeNoMove(
                        self.findKingJumps(self.board_vector, -2))
                    while (jm != []):
                        tp1 = jm
                        print("new jumps -", jm)
                        for i in jm:
                            if (i[0] == selMove[1]):
                                selMove = self.selectRandomInnerJump(i)
                                self.movePiece(selMove)
                                print("selected move", selMove)
                        if (jm == tp1):
                            break
                        jm = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1)) + self.removeNoMove(
                            self.findKingJumps(self.board_vector, -2))
            print("iteration:", c)
            self.showBoardV2()
            tester = self.__checkVictory()
            if tester == 'w':
                return 'w'
            elif tester == 'b':
                return 'b'
        return "d"

    # Test for a single checkers game run with a Neural Network.
    # Variable nn represents the neural network being used.
    # Neural Network is White. Random moves are Black.
    def gameTestNN_White(self, bool, nn):
        if bool:
            print("Game Start")
            self.showBoardV2()
            print("\n")
        testerNN = nn
        c = 0
        while (c < 100):
            c += 1
            if (c % 2 == 1):
                moves = self.removeNoMove(self.findSingleMoves(self.board_vector, 1))
                jumpmoves = self.removeNoMove(self.findJumps(self.board_vector, 1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, 2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, 2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps

                movesScores = []
                movesScoresJumps = []

                if bool:
                    print("\nall moves -", am)
                    print("all jumps -", jm)
                if (jm == [] and am == []):
                    # print("Black Victory. White can't move.")
                    return 'b'
                elif (jm == []):
                    cleanedAM = self.cleanArrayMoves(am)
                    if bool:
                        print("Cleaned Moves -", cleanedAM)
                    for i in range(len(cleanedAM)):
                        boardCopy = self.board_vector[:]
                        self.movePieceNN(boardCopy, cleanedAM[i])
                        movesScores.append(testerNN.feedForward(boardCopy))

                    maxIndex = self.indxOfMax(movesScores)
                    if bool:
                        print("Move scores -", movesScores)
                        print("selected move -", cleanedAM[maxIndex], "\n")
                    self.movePiece(cleanedAM[maxIndex])
                else:
                    cleanedJM = self.cleanArrayMoves(jm)
                    if bool:
                        print("Cleaned Jump Moves -", cleanedJM)
                    allJumps = []
                    for i in range(len(cleanedJM)):
                        tempjm = self.calculateJumpPaths(cleanedJM[i], self.board_vector[:])
                        allJumps.extend(self.createJumpPathsBuilder(tempjm))
                    if bool:
                        print("All Jumps -", allJumps)
                    for path in allJumps:
                        boardCopy = self.board_vector[:]
                        for jump in path:
                            self.movePieceNN(boardCopy, jump)
                        movesScoresJumps.append(testerNN.feedForward(boardCopy))

                    maxIndex = self.indxOfMax(movesScoresJumps)
                    if bool:
                        print("Move Jump scores -", movesScoresJumps)
                        print("selected move -", allJumps[maxIndex], "\n")
                    for jump in allJumps[maxIndex]:
                        self.movePieceNN(self.board_vector, jump)
            else:
                moves = self.removeNoMove(self.findSingleMovesReverse(self.board_vector, -1))
                jumpmoves = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, -2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, -2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps
                if bool:
                    print("\nall moves -", am)
                    print("all jumps -", jm, "\n")
                if (jm == [] and am == []):
                    # print("White Victory. Black can't move.")
                    return 'w'
                elif (jm == []):
                    selMove = self.selectRandomMove(am)
                    self.movePiece(selMove)
                    if bool:
                        print("selected move -", selMove)
                else:
                    selMove = self.selectRandomMove(jm)
                    self.movePiece(selMove)
                    if bool:
                        print("selected move", selMove)
                    jm = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1)) + self.removeNoMove(
                        self.findKingJumps(self.board_vector, -2))
                    while (jm != []):
                        tp1 = jm
                        if bool:
                            print("new jumps -", jm)
                        for i in jm:
                            if (i[0] == selMove[1]):
                                selMove = self.selectRandomInnerJump(i)
                                self.movePiece(selMove)
                                if bool:
                                    print("selected move", selMove)
                        if jm == tp1:
                            break
                        jm = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1)) + self.removeNoMove(
                            self.findKingJumps(self.board_vector, -2))
            if bool:
                print("iteration:", c)
                self.showBoardV2()
            tester = self.__checkVictory()
            if tester == 'w':
                return 'w'
            elif tester == 'b':
                return 'b'
        return "d"

    # Test for a single checkers game run with a Neural Network.
    # Variable nn represents the neural network being used.
    # Neural Network is Black. Random moves are White.
    def gameTestNN_Black(self, boole, nn):
        if boole:
            print("Game Start")
            self.showBoardV2()
            print("\n")
        testerNN = nn
        c = 0
        while (c < 100):
            c += 1
            if (c % 2 == 1):
                moves = self.removeNoMove(self.findSingleMoves(self.board_vector, 1))
                jumpmoves = self.removeNoMove(self.findJumps(self.board_vector, 1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, 2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, 2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps
                if boole:
                    print("\nall moves -", am)
                    print("all jumps -", jm, "\n")
                if (jm == [] and am == []):
                    # print("Black Victory. White can't move.")
                    return 'b'
                elif (jm == []):
                    selMove = self.selectRandomMove(am)
                    self.movePiece(selMove)
                    if boole:
                        print("selected move -", selMove)
                else:
                    selMove = self.selectRandomMove(jm)
                    self.movePiece(selMove)
                    if boole:
                        print("selected move", selMove)
                    jm = self.removeNoMove(self.findJumps(self.board_vector, 1)) + self.removeNoMove(
                        self.findKingJumps(self.board_vector, 2))
                    while (jm != []):
                        tp1 = jm
                        if boole:
                            print("new jumps -", jm)
                        for i in jm:
                            if (i[0] == selMove[1]):
                                selMove = self.selectRandomInnerJump(i)
                                self.movePiece(selMove)
                                if boole:
                                    print("selected move", selMove)
                        if (jm == tp1):
                            break
                        jm = self.removeNoMove(self.findJumps(self.board_vector, 1)) + self.removeNoMove(
                            self.findKingJumps(self.board_vector, 2))
            else:
                moves = self.removeNoMove(self.findSingleMovesReverse(self.board_vector, -1))
                jumpmoves = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, -2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, -2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps

                movesScores = []
                movesScoresJumps = []

                if boole:
                    print("\nall moves -", am)
                    print("all jumps -", jm)
                if (jm == [] and am == []):
                    # print("White Victory. Black can't move.")
                    return 'w'
                elif (jm == []):
                    cleanedAM = self.cleanArrayMoves(am)
                    if boole:
                        print("Cleaned Moves -", cleanedAM)
                    for i in range(len(cleanedAM)):
                        boardCopy = self.board_vector[:]
                        self.movePieceNN(boardCopy, cleanedAM[i])
                        movesScores.append(testerNN.feedForward(testerNN.convertBoardValues(boardCopy, -1)))

                    maxIndex = self.indxOfMax(movesScores)
                    if boole:
                        print("Move scores -", movesScores)
                        print("selected move -", cleanedAM[maxIndex], "\n")
                    self.movePiece(cleanedAM[maxIndex])
                else:
                    cleanedJM = self.cleanArrayMoves(jm)
                    if boole:
                        print("Cleaned Jump Moves -", cleanedJM)
                    allJumps = []
                    for i in range(len(cleanedJM)):
                        tempjm = self.calculateJumpPaths(cleanedJM[i], self.board_vector[:])
                        allJumps.extend(self.createJumpPathsBuilder(tempjm))
                    if boole:
                        print("All Jumps -", allJumps)
                    for path in allJumps:
                        boardCopy = self.board_vector[:]
                        for jump in path:
                            self.movePieceNN(boardCopy, jump)
                        movesScoresJumps.append(testerNN.feedForward(testerNN.convertBoardValues(boardCopy, -1)))

                    maxIndex = self.indxOfMax(movesScoresJumps)
                    if boole:
                        print("Move Jump scores -", movesScoresJumps)
                        print("selected move -", allJumps[maxIndex], "\n")
                    for jump in allJumps[maxIndex]:
                        self.movePieceNN(self.board_vector, jump)
            if boole:
                print("iteration:", c)
                self.showBoardV2()
            tester = self.__checkVictory()
            if tester == 'w':
                return 'w'
            elif tester == 'b':
                return 'b'
        return "d"

    # Test for a single checkers game run with a Neural Network.
    # Variable nn1 and nn2 represents the neural networks being used.
    # Neural Network 1 is White. Neural Network 2 is Black.
    # Variable bool prints out game information if True else is does not if False.
    def gameTestNN(self, bool, nn1, nn2):
        if bool:
            print("Game Start")
            self.showBoardV2()
            print("\n")
        c = 0
        while (c < 100):
            c += 1
            if (c % 2 == 1):
                moves = self.removeNoMove(self.findSingleMoves(self.board_vector, 1))
                jumpmoves = self.removeNoMove(self.findJumps(self.board_vector, 1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, 2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, 2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps

                movesScores = []
                movesScoresJumps = []

                if bool:
                    print("\nall moves -", am)
                    print("all jumps -", jm)
                if (jm == [] and am == []):
                    # print("Black Victory. White can't move.")
                    return 'b'
                elif (jm == []):
                    cleanedAM = self.cleanArrayMoves(am)
                    if bool:
                        print("Cleaned Moves -", cleanedAM)
                    for i in range(len(cleanedAM)):
                        boardCopy = self.board_vector[:]
                        self.movePieceNN(boardCopy, cleanedAM[i])
                        movesScores.append(nn1.feedForward(boardCopy))

                    maxIndex = self.indxOfMax(movesScores)
                    if bool:
                        print("Move scores -", movesScores)
                        print("selected move -", cleanedAM[maxIndex], "\n")
                    self.movePiece(cleanedAM[maxIndex])
                else:
                    cleanedJM = self.cleanArrayMoves(jm)
                    if bool:
                        print("Cleaned Jump Moves -", cleanedJM)
                    allJumps = []
                    for i in range(len(cleanedJM)):
                        tempjm = self.calculateJumpPaths(cleanedJM[i], self.board_vector[:])
                        allJumps.extend(self.createJumpPathsBuilder(tempjm))
                    if bool:
                        print("All Jumps -", allJumps)
                    for path in allJumps:
                        boardCopy = self.board_vector[:]
                        for jump in path:
                            self.movePieceNN(boardCopy, jump)
                        movesScoresJumps.append(nn1.feedForward(boardCopy))

                    maxIndex = self.indxOfMax(movesScoresJumps)
                    if bool:
                        print("Move Jump scores -", movesScoresJumps)
                        print("selected move -", allJumps[maxIndex], "\n")
                    for jump in allJumps[maxIndex]:
                        self.movePieceNN(self.board_vector, jump)
            else:
                moves = self.removeNoMove(self.findSingleMovesReverse(self.board_vector, -1))
                jumpmoves = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, -2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, -2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps

                movesScores = []
                movesScoresJumps = []

                if bool:
                    print("\nall moves -", am)
                    print("all jumps -", jm)
                if (jm == [] and am == []):
                    # print("White Victory. Black can't move.")
                    return 'w'
                elif (jm == []):
                    cleanedAM = self.cleanArrayMoves(am)
                    if bool:
                        print("Cleaned Moves -", cleanedAM)
                    for i in range(len(cleanedAM)):
                        boardCopy = self.board_vector[:]
                        self.movePieceNN(boardCopy, cleanedAM[i])
                        movesScores.append(nn2.feedForward(boardCopy))

                    maxIndex = self.indxOfMax(movesScores)
                    if bool:
                        print("Move scores -", movesScores)
                        print("selected move -", cleanedAM[maxIndex], "\n")
                    self.movePiece(cleanedAM[maxIndex])
                else:
                    cleanedJM = self.cleanArrayMoves(jm)
                    if bool:
                        print("Cleaned Jump Moves -", cleanedJM)
                    allJumps = []
                    for i in range(len(cleanedJM)):
                        tempjm = self.calculateJumpPaths(cleanedJM[i], self.board_vector[:])
                        allJumps.extend(self.createJumpPathsBuilder(tempjm))
                    if bool:
                        print("All Jumps -", allJumps)
                    for path in allJumps:
                        boardCopy = self.board_vector[:]
                        for jump in path:
                            self.movePieceNN(boardCopy, jump)
                        movesScoresJumps.append(nn2.feedForward(boardCopy))

                    maxIndex = self.indxOfMax(movesScoresJumps)
                    if bool:
                        print("Move Jump scores -", movesScoresJumps)
                        print("selected move -", allJumps[maxIndex], "\n")
                    for jump in allJumps[maxIndex]:
                        self.movePieceNN(self.board_vector, jump)
            if bool:
                print("iteration:", c)
                self.showBoardV2()
            tester = self.__checkVictory()
            if tester == 'w':
                return 'w'
            elif tester == 'b':
                return 'b'
        return "d"

    # Plays a number of n games.
    # Variable n is an integer for number of games to be played. Variable boolean either True or False to show game board.
    def run(self, n, boolean):
        wv = 0
        bv = 0
        draw = 0
        start = time.time()
        for i in range(1, n + 1):
            if (i / n * 100) % 5 == 0:
                print(str(int(i / n * 100)) + "% ", end='', flush=True)
            if i == n:
                print('\n')
            winner = self.game(boolean)
            if (winner == 'w'):
                wv += 1
            elif (winner == 'b'):
                bv += 1
            elif (winner == 'd'):
                draw += 1
        end = time.time()
        print("_____", n, "games played _____")
        print("\nTime taken: %.2f seconds." % (end - start))
        print("White won", wv, "times. = %.2f" % (wv / n * 100), "%")
        print("Black won", bv, "times. = %.2f" % (bv / n * 100), "%")
        print("Draw", draw, "times. = %.2f" % (draw / n * 100), "%")

    # Game for a single checkers game run with a Neural Network.
    # Variable nn represents the neural network being used.
    # Neural Network is White. Player moves are Black.
    def playGameAsBlack(self, bool, nn):
        print("Game Start")
        self.showBoardV2()
        print("\n")
        testerNN = nn
        c = 0
        while (c < 100):
            c += 1
            if (c % 2 == 1):
                print("White's Turn.")
                moves = self.removeNoMove(self.findSingleMoves(self.board_vector, 1))
                jumpmoves = self.removeNoMove(self.findJumps(self.board_vector, 1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, 2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, 2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps

                movesScores = []
                movesScoresJumps = []

                if bool:
                    print("\nall moves -", am)
                    print("all jumps -", jm)
                if (jm == [] and am == []):
                    print("Black Victory. White can't move.")
                    return 'b'
                elif (jm == []):
                    cleanedAM = self.cleanArrayMoves(am)
                    if bool:
                        print("Cleaned Moves -", cleanedAM)
                    for i in range(len(cleanedAM)):
                        boardCopy = self.board_vector[:]
                        self.movePieceNN(boardCopy, cleanedAM[i])
                        movesScores.append(testerNN.feedForward(boardCopy))

                    maxIndex = self.indxOfMax(movesScores)
                    if bool:
                        print("Move scores -", movesScores)
                    print("selected move -", cleanedAM[maxIndex], "\n")
                    self.movePiece(cleanedAM[maxIndex])
                else:
                    cleanedJM = self.cleanArrayMoves(jm)
                    if bool:
                        print("Cleaned Jump Moves -", cleanedJM)
                    allJumps = []
                    for i in range(len(cleanedJM)):
                        tempjm = self.calculateJumpPaths(cleanedJM[i], self.board_vector[:])
                        allJumps.extend(self.createJumpPathsBuilder(tempjm))
                    if bool:
                        print("All Jumps -", allJumps)
                    for path in allJumps:
                        boardCopy = self.board_vector[:]
                        for jump in path:
                            self.movePieceNN(boardCopy, jump)
                        movesScoresJumps.append(testerNN.feedForward(boardCopy))

                    maxIndex = self.indxOfMax(movesScoresJumps)
                    if bool:
                        print("Move Jump scores -", movesScoresJumps)
                    print("selected move -", allJumps[maxIndex], "\n")
                    for jump in allJumps[maxIndex]:
                        self.movePieceNN(self.board_vector, jump)
            else:
                print("Black's Turn.")
                moves = self.removeNoMove(self.findSingleMovesReverse(self.board_vector, -1))
                jumpmoves = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, -2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, -2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps
                if bool:
                    print("\nall moves -", am)
                    print("all jumps -", jm, "\n")
                if (jm == [] and am == []):
                    print("White Victory. Black can't move.")
                    return 'w'
                else:
                    tmove = input(
                        "Please enter a move in the form \"piece destination\". Both being the number corresponding to the board position.\n>> ")
                    move = tmove.split(" ")
                    move[0] = int(move[0])
                    move[1] = int(move[1])
                    self.movePiece(move)
                    while input("Is there a jump?") == "y":
                        tmove = input(
                            "Please enter a move in the form \"piece destination\". Both being the number corresponding to the board position.\n>> ")
                        move = tmove.split(" ")
                        move[0] = int(move[0])
                        move[1] = int(move[1])
                        self.movePiece(move)
            self.showBoardV2()
            tester = self.__checkVictory()
            if tester == 'w':
                return 'w'
            elif tester == 'b':
                return 'b'
        return "d"

    # Game for a single checkers game run with a Neural Network.
    # Variable nn represents the neural network being used.
    # Neural Network is White. Player moves are Black.
    def playGameAsWhite(self, bool, nn):
        print("Game Start")
        self.showBoardV3()
        print("\n")
        testerNN = nn
        c = 0
        while (c < 100):
            c += 1
            if (c % 2 == 1):
                print("White's Turn.")
                moves = self.removeNoMove(self.findSingleMoves(self.board_vector, 1))
                jumpmoves = self.removeNoMove(self.findJumps(self.board_vector, 1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, 2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, 2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps
                if bool:
                    print("\nall moves -", am)
                    print("all jumps -", jm)
                if (jm == [] and am == []):
                    print("Black Victory. White can't move.")
                    return 'b'
                else:
                    if jm != []:
                        print("Jump available!")
                    self.showBoardIndices()
                    tmove = input(
                        "Please enter a move in the form \"piece destination\". Both being the number corresponding to the board position.\n>> ")
                    move = tmove.split(" ")
                    move[0] = int(move[0])
                    move[1] = int(move[1])
                    while True:
                        if [move[0], move[1]] in self.cleanArrayMoves(am) or [move[0], move[1]] in self.cleanArrayMoves(
                                jm):
                            self.movePiece(move)
                            break
                        else:
                            print("\nMove not possible.")
                            tmove = input(
                                "Please enter a move in the form \"piece destination\". Both being the number corresponding to the board position.\n>> ")
                            move = tmove.split(" ")
                            move[0] = int(move[0])
                            move[1] = int(move[1])

                    if jm != []:
                        while input("Is there another jump?") == "y":
                            tmove = input(
                                "Please enter a move in the form \"piece destination\". Both being the number corresponding to the board position.\n>> ")
                            move = tmove.split(" ")
                            move[0] = int(move[0])
                            move[1] = int(move[1])
                            self.movePiece(move)
            else:
                print("Black's Turn.")
                time.sleep(3)
                moves = self.removeNoMove(self.findSingleMovesReverse(self.board_vector, -1))
                jumpmoves = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1))
                kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, -2))
                kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, -2))
                am = moves + kingmoves
                jm = jumpmoves + kingjumps

                movesScores = []
                movesScoresJumps = []

                if bool:
                    print("\nall moves -", am)
                    print("all jumps -", jm)
                if (jm == [] and am == []):
                    print("White Victory. Black can't move.")
                    return 'w'
                elif (jm == []):
                    cleanedAM = self.cleanArrayMoves(am)
                    if bool:
                        print("Cleaned Moves -", cleanedAM)
                    for i in range(len(cleanedAM)):
                        boardCopy = self.board_vector[:]
                        self.movePieceNN(boardCopy, cleanedAM[i])
                        movesScores.append(testerNN.feedForward(testerNN.convertBoardValues(boardCopy, -1)))

                    maxIndex = self.indxOfMax(movesScores)
                    if bool:
                        print("Move scores -", movesScores)
                    print("selected move -", cleanedAM[maxIndex], "\n")
                    self.movePiece(cleanedAM[maxIndex])
                else:
                    cleanedJM = self.cleanArrayMoves(jm)
                    if bool:
                        print("Cleaned Jump Moves -", cleanedJM)
                    allJumps = []
                    for i in range(len(cleanedJM)):
                        tempjm = self.calculateJumpPaths(cleanedJM[i], self.board_vector[:])
                        allJumps.extend(self.createJumpPathsBuilder(tempjm))
                    if bool:
                        print("All Jumps -", allJumps)
                    for path in allJumps:
                        boardCopy = self.board_vector[:]
                        for jump in path:
                            self.movePieceNN(boardCopy, jump)
                        movesScoresJumps.append(testerNN.feedForward(testerNN.convertBoardValues(boardCopy, -1)))

                    maxIndex = self.indxOfMax(movesScoresJumps)
                    if bool:
                        print("Move Jump scores -", movesScoresJumps)
                    print("selected move -", allJumps[maxIndex], "\n")
                    for jump in allJumps[maxIndex]:
                        self.movePieceNN(self.board_vector, jump)
            time.sleep(1)
            self.showBoardV3()
            tester = self.__checkVictory()
            if tester == 'w':
                return 'w'
            elif tester == 'b':
                return 'b'
        return "d"

    def liveGameRunner(self):
        result = 0
        play_as = input("Black or white?\n>> ")
        if play_as == "black":
            result = self.playGameAsBlack(False, self.whiteNN)
        elif play_as == "white":
            result = self.playGameAsWhite(False, self.blackNN)

        if result == "w":
            print("***** White Wins!! *****")
        elif result == "b":
            print("***** Black Wins!! *****")

    ####################################################################################
    # GUI Functions

    def hasJump(self, index):
        jump = 0
        if self.board_vector[index] == 2 or self.board_vector[index] == -2:
            jump = self.findKingJumpsSinglePiece(self.board_vector, index, self.board_vector[index])
        else:
            if self.board_vector[index] == 1:
                jump = self.findJumpsSinglePiece(self.board_vector, index, self.board_vector[index])
            elif self.board_vector[index] == -1:
                jump = self.findJumpsReverseSinglePiece(self.board_vector, index, self.board_vector[index])
            else:
                return "error"
        jump = self.removeNegatives(jump)
        # print("move =", jump)
        return len(jump) != 0

    def set_gui_player(self, player):
        self.gui_player = player

    def gui_check(self, c, move):
        if self.gui_player == "White":
            if (c % 2) == 1:
                return self.gui_playGameAsWhite_Player(move)  # Takes in move to be made.
                #return self.gui_playGameAsWhite_Opponant()
            else:
                return self.guiplaygameasWhite_minimaxai()
                #return self.gui_playGameAsWhite_Opponant()  # Returns move to be made.
        elif self.gui_player == "Red":
            if (c % 2) == 0:
                return self.gui_playGameAsBlack_Player(move)  # Takes in move to be made.
            else:
                #return self.guiplaygameasBlack_minimaxai()
                return self.gui_playGameAsBlack_Opponant()
        else:
            print("Player Error. Incorrect Player type.")

    # runs check on move passed to it. Playing as the Red/Black player.
    def gui_playGameAsBlack_Player(self, move):
        moves = self.removeNoMove(self.findSingleMovesReverse(self.board_vector, -1))
        jumpmoves = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1))
        kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, -2))
        kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, -2))
        am = moves + kingmoves
        jm = jumpmoves + kingjumps
        if (jm == [] and am == []):
            return 'b'
        else:
            if move in self.cleanArrayMoves(am) or move in self.cleanArrayMoves(jm):
                if move in self.cleanArrayMoves(am) and jm != []:
                    return [False, False]
                else:
                    self.movePiece(move)
                # print("In Brain.  Making Move.", move)
                if self.hasJump(move[1]):
                    return [True, True]
                else:
                    return [True, False]
            else:
                return [False, False]

    # Returns the move to be made by the opponant. Playing as the Red/Black player.
    def gui_playGameAsBlack_Opponant(self):
        testerNN = self.whiteNN
        #time.sleep(2)

        moves = self.removeNoMove(self.findSingleMoves(self.board_vector, 1))
        jumpmoves = self.removeNoMove(self.findJumps(self.board_vector, 1))
        kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, 2))
        kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, 2))
        am = moves + kingmoves
        jm = jumpmoves + kingjumps

        movesScores = []
        movesScoresJumps = []

        if (jm == [] and am == []):
            return 'b'
        elif (jm == []):
            cleanedAM = self.cleanArrayMoves(am)
            for i in range(len(cleanedAM)):
                boardCopy = self.board_vector[:]
                self.movePieceNN(boardCopy, cleanedAM[i])
                movesScores.append(testerNN.feedForward(boardCopy))

            maxIndex = self.indxOfMax(movesScores)
            self.movePiece(cleanedAM[maxIndex])
            return cleanedAM[maxIndex]
        else:
            cleanedJM = self.cleanArrayMoves(jm)
            allJumps = []
            for i in range(len(cleanedJM)):
                tempjm = self.calculateJumpPaths(cleanedJM[i], self.board_vector[:])
                allJumps.extend(self.createJumpPathsBuilder(tempjm))
            for path in allJumps:
                boardCopy = self.board_vector[:]
                for jump in path:
                    self.movePieceNN(boardCopy, jump)
                movesScoresJumps.append(testerNN.feedForward(boardCopy))

            maxIndex = self.indxOfMax(movesScoresJumps)
            for jump in allJumps[maxIndex]:
                self.movePieceNN(self.board_vector, jump)
            return allJumps[maxIndex]

    # runs check on move passed to it. Playing as the White player.
    def gui_playGameAsWhite_Player(self, move):
        moves = self.removeNoMove(self.findSingleMoves(self.board_vector, 1))
        jumpmoves = self.removeNoMove(self.findJumps(self.board_vector, 1))
        kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, 2))
        kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, 2))
        am = moves + kingmoves
        jm = jumpmoves + kingjumps
        if (jm == [] and am == []):
            return 'b'
        else:
            if move in self.cleanArrayMoves(am) or move in self.cleanArrayMoves(jm):
                if move in self.cleanArrayMoves(am) and jm != []:
                    return [False, False]
                else:
                    self.movePiece(move)
                # print("In Brain.  Making Move.", move)
                if self.hasJump(move[1]):
                    return [True, True]
                else:
                    return [True, False]
            else:
                return [False, False]

    # Returns the move to be made by the opponant. Playing as the White player.
    def gui_playGameAsWhite_Opponant(self):
        testerNN = self.blackNN
        #time.sleep(2)

        moves = self.removeNoMove(self.findSingleMovesReverse(self.board_vector, -1))
        jumpmoves = self.removeNoMove(self.findJumpsReverse(self.board_vector, -1))
        kingmoves = self.removeNoMove(self.findKingMoves(self.board_vector, -2))
        kingjumps = self.removeNoMove(self.findKingJumps(self.board_vector, -2))
        am = moves + kingmoves
        jm = jumpmoves + kingjumps

        movesScores = []
        movesScoresJumps = []

        if (jm == [] and am == []):
            return 'w'
        elif (jm == []):
            cleanedAM = self.cleanArrayMoves(am)
            for i in range(len(cleanedAM)):
                boardCopy = self.board_vector[:]
                self.movePieceNN(boardCopy, cleanedAM[i])
                movesScores.append(testerNN.feedForward(testerNN.convertBoardValues(boardCopy, -1)))

            maxIndex = self.indxOfMax(movesScores)
            self.movePiece(cleanedAM[maxIndex])
            return cleanedAM[maxIndex]
        else:
            cleanedJM = self.cleanArrayMoves(jm)
            allJumps = []
            for i in range(len(cleanedJM)):
                tempjm = self.calculateJumpPaths(cleanedJM[i], self.board_vector[:])
                allJumps.extend(self.createJumpPathsBuilder(tempjm))
            for path in allJumps:
                boardCopy = self.board_vector[:]
                for jump in path:
                    self.movePieceNN(boardCopy, jump)
                movesScoresJumps.append(testerNN.feedForward(testerNN.convertBoardValues(boardCopy, -1)))

            maxIndex = self.indxOfMax(movesScoresJumps)
            for jump in allJumps[maxIndex]:
                self.movePieceNN(self.board_vector, jump)
            return allJumps[maxIndex]

    # Test to see whether there is a victor.
    # Variable c is the turn counter.
    # Returns end result or false if game is not over.
    def gui_Victory_Check(self, c):
        tester = self.__checkVictory()
        if tester == 'w':
            return 'w'
        elif tester == 'b':
            return 'b'
        elif c == 100:
            return "d"
        else:
            return False

    def guiplaygameasWhite_minimaxai(self):
        #time.sleep(2)
        return self.get_best_move(board = self, color = "black")


    def guiplaygameasBlack_minimaxai(self):
        #time.sleep(2)
        return self.get_best_move(board = self, color = "white")


    def getheuristic(self):
        piece_values = {
            1: 1,  # Regular white piece
            2: 3,  # King white piece
            -1: -1,  # Regular black piece
            -2: -3   # King black piece
        }
        score = 0
        for piece in self.board_vector:
            score += piece_values.get(piece, 0)
        return score

    def evaluate_kings(self):
    # Evaluate the presence and positions of kings
        king_value = 5  # Adjust the weight of kings as needed
        king_count = 0
        for i in self.board_vector:
            if i == 2:
                king_count += 1
            elif i == -2:
                king_count -= 1
        return king_count * king_value

 ####fix
    def minimax(self, board, depth, maximizing_player, alpha, beta, color: str):
        temp = 1 if color == "white" else -1

    # Check for terminal states or depth limit
        if depth == 0 or Checkers.checkend(board):
            return board.getheuristic(), None

        if maximizing_player:
            max_eval = float('-inf')
            best_move = None

        # Generate possible moves
            if color == "black":
                moves = board.removeNoMove(board.findSingleMovesReverse(board.board_vector[:], temp))
                jumpmoves = board.removeNoMove(board.findJumpsReverse(board.board_vector[:], temp))
            else:
                moves = board.removeNoMove(board.findSingleMoves(board.board_vector[:], temp))
                jumpmoves = board.removeNoMove(board.findJumps(board.board_vector[:], temp))

            kingmoves = board.removeNoMove(board.findKingMoves(board.board_vector[:], temp * 2))
            kingjumps = board.removeNoMove(board.findKingJumps(board.board_vector[:], temp * 2))

            am = moves + kingmoves
            jm = jumpmoves + kingjumps

            if not am and not jm:
                return board.getheuristic(), None  # Return heuristic for terminal state

            if not jm:
                moves = board.cleanArrayMoves(am)
                if not moves:
                    return board.getheuristic(), None  # No valid moves available

                for move in moves:
                    new_board = deepcopy(board)
                    new_board.movePiece(move)
                    eval, _ = self.minimax(new_board, depth - 1, False, alpha, beta, "black" if color == "white" else "white")
                    if eval > max_eval:
                        max_eval = eval
                        best_move = move
                    alpha = max(alpha, max_eval)
                    if beta <= alpha:
                        break  # Beta cut-off
                return max_eval, best_move
            else:
                moves = board.cleanArrayMoves(jm)
                if not moves:
                    return board.getheuristic(), None  # No valid jump moves available

                allJumps = []
                for jm in moves:
                    tempjm = board.calculateJumpPaths(jm, board.board_vector[:])
                    allJumps.extend(board.createJumpPathsBuilder(tempjm))
                moves = allJumps

                for move in moves:
                    new_board = deepcopy(board)
                    for jump in move:
                        new_board.movePiece(jump)
                    eval, _ = self.minimax(new_board, depth - 1, False, alpha, beta, "black" if color == "white" else "white")
                    if eval > max_eval:
                        max_eval = eval
                        best_move = move
                    alpha = max(alpha, max_eval)
                    if beta <= alpha:
                        break  # Beta cut-off
                return max_eval, best_move

        else:
            min_eval = float('inf')
            best_move = None

        # Generate possible moves
            if color == "black":
                moves = board.removeNoMove(board.findSingleMovesReverse(board.board_vector[:], temp))
                jumpmoves = board.removeNoMove(board.findJumpsReverse(board.board_vector[:], temp))
            else:
                moves = board.removeNoMove(board.findSingleMoves(board.board_vector[:], temp))
                jumpmoves = board.removeNoMove(board.findJumps(board.board_vector[:], temp))

            kingmoves = board.removeNoMove(board.findKingMoves(board.board_vector[:], temp * 2))
            kingjumps = board.removeNoMove(board.findKingJumps(board.board_vector[:], temp * 2))

            am = moves + kingmoves
            jm = jumpmoves + kingjumps

            if not am and not jm:
                return board.getheuristic(), None  # Return heuristic for terminal state

            if not jm:
                moves = board.cleanArrayMoves(am)
                if not moves:
                    return board.getheuristic(), None  # No valid moves available

                for move in moves:
                    new_board = deepcopy(board)
                    new_board.movePiece(move)
                    eval, _ = self.minimax(new_board, depth - 1, True, alpha, beta, "black" if color == "white" else "white")
                    if eval < min_eval:
                        min_eval = eval
                        best_move = move
                    beta = min(beta, min_eval)
                    if beta <= alpha:
                        break  # Alpha cut-off
                return min_eval, best_move
            else:
                moves = board.cleanArrayMoves(jm)
                if not moves:
                    return board.getheuristic(), None  # No valid jump moves available

                allJumps = []
                for jm in moves:
                    tempjm = board.calculateJumpPaths(jm, board.board_vector[:])
                    allJumps.extend(board.createJumpPathsBuilder(tempjm))
                moves = allJumps

                for move in moves:
                    new_board = deepcopy(board)
                    for jump in move:
                        new_board.movePiece(jump)
                    eval, _ = self.minimax(new_board, depth - 1, True, alpha, beta, "black" if color == "white" else "white")
                    if eval < min_eval:
                        min_eval = eval
                        best_move = move
                    beta = min(beta, min_eval)
                    if beta <= alpha:
                        break  # Alpha cut-off
                return min_eval, best_move  #moves = board.flattenJumpPathArray(moves)

    def countPieces(self, color):
        count = 0
        for piece in self.board_vector:
            if piece == 1 and color == 'w':
                count += 1
            elif piece == -1 and color == 'b':
                count += 1
        return count
    
    def get_best_move(self, board, color : str):
        eval, best_move = self.minimax(board=board, depth=self.depth, maximizing_player=True, alpha=float('-inf'), beta=float('inf'), color=color)

        if best_move is not None:
            if isinstance(best_move[0], list):
                for move in best_move:
                    board.movePiece(move)
            else:
                board.movePiece(best_move)
        else:
        # If there is no best move, make a move that prevents the game from getting stuck in a draw
            moves, jumpmoves = self.get_moves(board, color, 1 if color == "white" else -1)
            if moves or jumpmoves:
                if jumpmoves:
                    moves = board.cleanArrayMoves(jumpmoves)
                else:
                    moves = board.cleanArrayMoves(moves)
                if moves:
                    best_move = moves[0]  # Make the first available move
                    if isinstance(best_move[0], list):
                        for move in best_move:
                            board.movePiece(move)
                    else:
                        board.movePiece(best_move)

        return best_move
    
    def get_moves(self, board, color, direction):
        moves = []
        jump_moves = []
        for i in range(len(board.board_vector)):
            piece = board.board_vector[i]
            if (piece == 1 and color == 'white') or (piece == -1 and color == 'black') or (piece == 2 and color == 'white') or (piece == -2 and color == 'black'):
                moves.extend(self.get_single_moves(board, i, direction))
                jump_moves.extend(self.get_jump_moves(board, i, direction))
        return moves, jump_moves

    def get_single_moves(self, board, index, direction):
        moves = []
        if index + direction >= 0 and index + direction < len(board.board_vector) and board.board_vector[index + direction] == 0:
            moves.append([index, index + direction])
        return moves

    def get_jump_moves(self, board, index, direction):
        jump_moves = []
        if index + (2 * direction) >= 0 and index + (2 * direction) < len(board.board_vector):
            if board.board_vector[index + direction] != 0 and board.board_vector[index + (2 * direction)] == 0:
                jump_moves.append([index, index + (2 * direction)])
        return jump_moves


    def gameTestNNvsminmax(self, bool):
        if bool:
            print("Game Start")
            self.showBoardV3()
            print("\n")
    
        c = 0
        self.movePiece(self.selectRandomMove(self.findSingleMoves(self.board_vector[:],1)))
        self.movePiece(self.selectRandomMove(self.findSingleMovesReverse(self.board_vector[:],-1)))
    
        prev_white_pieces = self.countPieces('w')
        prev_black_pieces = self.countPieces('b')
        d=0
        while (c < 10000):
            c += 1
            if (c % 2 == 1):
                self.guiplaygameasWhite_minimaxai() #moves white
            else:
                best_move = self.gui_playGameAsBlack_Opponant() #moves black

            if bool:
                print("iteration:", c)
                d+=1
                self.showBoardV3()

            tester = self.__checkVictory()
            if tester == 'w':
                return 'w'
            elif tester == 'b':
                return 'b'

        # Check if the game has been running for more than 300 iterations
            if d > 300:
                white_pieces = self.countPieces('w')
                black_pieces = self.countPieces('b')
               # print(prev_black_pieces, c, black_pieces, white_pieces, black_pieces)
            # If the number of pieces hasn't changed significantly, declare the winner based on piece count
                if abs(white_pieces - prev_white_pieces) <= 1 and abs(black_pieces - prev_black_pieces) <= 1:
                    if white_pieces > black_pieces:
                        return 'w'
                    elif black_pieces > white_pieces:
                        return 'b'
                    else:
                        return 'd'

                prev_white_pieces = white_pieces
                prev_black_pieces = black_pieces

        return "d"


game = Checkers(True)

wv = 0
bv = 0
draw = 0
start = time.time()
n = 1
for i in range(1, n + 1): 
     if (i / n * 100) % 5 == 0:
         print(str(int(i / n * 100)) + "% ", end='', flush=True)
     if i == n:
        print('\n')
     winner = game.gameTestNNvsminmax(True)
     game.setBoard()
     if (winner == 'w'):
         wv += 1
     elif (winner == 'b'):
         bv += 1
     elif (winner == 'd'):
         draw += 1
end = time.time()
print("_____", n, "games played _____")
print("\nTime taken: %.2f seconds." % (end - start))
print("White won", wv, "times. = %.2f" % (wv / n * 100), "%")
print("Black won", bv, "times. = %.2f" % (bv / n * 100), "%")
print("Draw", draw, "times. = %.2f" % (draw / n * 100), "%")
