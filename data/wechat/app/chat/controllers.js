angular.module('chat.controllers', ['chat.services', 'ngCookies'])
    .controller('CtrlChat', ['$scope', '$rootScope', '$uibModal', 'PATH', 'Quickblox',
        function ($scope, $rootScope, $uibModal, PATH, Quickblox) {

            $rootScope.title = 'CHAT Yo-hoo';
            $scope.qb = Quickblox;
            $scope.qb.connect();
            $scope.msg = {body: null};

            $scope.send_message = function () {
                $scope.qb.send_message($scope.qb.current_dialog, $scope.msg.body);
                $scope.msg.body = null;
            };
            $scope.$on('ChatMessage', function () {
                $scope.$apply();
            });
            $scope.open_user_list = function () {
                // TODO search
                var modalInstance = $uibModal.open({
                    animation: true,
                    templateUrl: PATH + 'chat/templates/test/modal_users.html',
                    controller: 'ChatUserListCtrl',
                    size: 'sm',
                    resolve: {
                        qb: function () {
                            return $scope.qb;
                        }
                    }
                });

            }

        }
    ])
    .controller('ChatUserListCtrl', ['$scope', '$translate', '$uibModalInstance', 'qb',
        function ($scope, $translate, $uibModalInstance, qb) {
            $scope.qb = qb;
            $scope.cancel = function () {
                $uibModalInstance.dismiss('cancel');
            }
        }

    ]);
